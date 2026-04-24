import json

def lookup_domain_info(domain: str) -> str:
    """
    Looks up and returns mock company information based on its domain.
    """
    print(f"-> TOOL ACTIVATED: Looking up domain info for {domain}...")

    mock_data = {
        "acmecorp.com": {"industry": "Software/SaaS", "size": "501-1000 employees", "revenue": "$50M - $100M"},
        "widgetco.net": {"industry": "Manufacturing", "size": "100-250 employees", "revenue": "$10M - $25M"},
        "globalfin.org": {"industry": "Financial Services", "size": "5000+ employees", "revenue": "$1B+"},
    }

    info = mock_data.get(domain, {"industry": "Unknown", "size": "N/A", "revenue": "N/A"})
    return json.dumps(info)
