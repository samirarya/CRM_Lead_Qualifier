import json
from ..config import get_client
from .schemas import TOOLS_SCHEMA
from ..tools.enrichment import lookup_domain_info
from ..tools.crm import check_crm_history
from ..tools.scoring import calculate_lead_score

AVAILABLE_FUNCTIONS = {
    "lookup_domain_info": lookup_domain_info,
    "check_crm_history": check_crm_history,
    "calculate_lead_score": calculate_lead_score,
}

def run_agent(user_prompt: str):
    """
    The main execution loop for the CRM Lead Qualifier Agent.
    """
    client = get_client()
    print(f"\n--- Running Lead Qualifier Agent ---")

    system_prompt = (
        "You are an expert CRM Lead Qualifier Agent. Your sole task is to analyze a sales lead "
        "provided via email address. You must follow these steps precisely: "
        "1. Identify the domain from the email. "
        "2. Call `lookup_domain_info` and `check_crm_history` sequentially to gather all data. "
        "3. Combine all collected data into a single JSON object. "
        "4. Call `calculate_lead_score` with the combined JSON object. "
        "5. Finally, synthesize all information (domain info, CRM history, and score) "
        "into a single, easy-to-read summary for a busy sales rep."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    collected_data = {}

    while True:
        print("\n[AI Thinking...]")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=TOOLS_SCHEMA,
            tool_choice="auto",
        )

        response_message = response.choices[0].message
        messages.append(response_message)

        if response_message.tool_calls:
            tool_calls = response_message.tool_calls

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_to_call = AVAILABLE_FUNCTIONS.get(function_name)
                
                try:
                    function_args = json.loads(tool_call.function.arguments)
                except json.JSONDecodeError:
                    print(f"Error decoding arguments for {function_name}")
                    continue

                if not function_to_call:
                    print(f"Error: Unknown function {function_name}")
                    continue

                # Execute the function
                if function_name == "calculate_lead_score":
                    # Inject the accumulated data from previous turns
                    function_args = {"data_summary": json.dumps(collected_data)}
                    function_result = function_to_call(**function_args)
                else:
                    function_result = function_to_call(**function_args)

                # Update the persistent memory (collected_data)
                if function_name == "lookup_domain_info":
                    collected_data["domain_info"] = json.loads(function_result)
                elif function_name == "check_crm_history":
                    collected_data["crm_history"] = json.loads(function_result)

                # Append the tool result as a NEW message
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": function_result
                })

        else:
            print("\n--- FINAL AGENT SUMMARY ---")
            print(response_message.content)
            break
