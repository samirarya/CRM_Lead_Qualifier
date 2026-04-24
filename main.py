from crm_agent.core.engine import run_agent

def main():
    # Scenario 1: High-Value Lead
    lead_email_1 = "jane@acmecorp.com"
    print(f"Testing Scenario 1: {lead_email_1}")
    try:
        run_agent(f"Please qualify this lead for my call tomorrow: {lead_email_1}")
    except Exception as e:
        print(f"Error running agent: {e}")

    print("\n" + "="*80 + "\n")

    # Scenario 2: Medium-Value Lead
    lead_email_2 = "bob@widgetco.net"
    print(f"Testing Scenario 2: {lead_email_2}")
    try:
        run_agent(f"Can you run an analysis on this lead: {lead_email_2}")
    except Exception as e:
        print(f"Error running agent: {e}")

if __name__ == "__main__":
    main()
