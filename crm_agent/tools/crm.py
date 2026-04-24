import json

def check_crm_history(email: str) -> str:
    """
    Checks the internal CRM system for past engagement history.
    """
    print(f"-> TOOL ACTIVATED: Checking CRM history for {email}...")

    mock_data = {
        "jane@acmecorp.com": {"last_contact": "2025-11-15", "status": "Cold Lead", "notes": "Attended webinar, no follow-up yet."},
        "bob@widgetco.net": {"last_contact": "2025-12-01", "status": "Active Opportunity", "notes": "Discussed Q1 budget and product integration."},
        "default": {"last_contact": "N/A", "status": "No Record", "notes": "New lead, first contact opportunity."},
    }

    history = mock_data.get(email, mock_data["default"])
    return json.dumps(history)
