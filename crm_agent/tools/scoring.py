import json

def calculate_lead_score(data_summary: str) -> str:
    """
    Analyzes collected data to assign a lead score.
    """
    print("-> TOOL ACTIVATED: Calculating lead score...")

    try:
        data = json.loads(data_summary)
    except json.JSONDecodeError:
        return json.dumps({"lead_score": "Error parsing data"})

    score = "Low"
    
    domain_info = data.get("domain_info", {})
    crm_history = data.get("crm_history", {})

    if domain_info.get("revenue", "").startswith("$1B+"):
        score = "High"
    elif crm_history.get("status") == "Active Opportunity":
        score = "High"
    elif domain_info.get("revenue", "").startswith("$50M"):
        score = "Medium"

    return json.dumps({"lead_score": score})
