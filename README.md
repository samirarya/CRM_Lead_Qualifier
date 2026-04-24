# CRM Lead Qualifier Agent

An intelligent AI agent built with Python and OpenAI's Function Calling capability. This agent automates the process of researching sales leads, checking internal CRM history, and calculating a priority score.

## Features

- **Automated Enrichment**: Extracts domains from email addresses and simulates looking up company data (industry, size, revenue).
- **CRM Integration**: Simulates checking internal records for past engagements and notes.
- **Smart Scoring**: Uses a logical scoring engine to prioritize leads as High, Medium, or Low.
- **Modular Architecture**: Cleanly separated into tools, agent core, and configuration modules.

## Project Structure

```text
crm_lead_qualifier/
├── crm_agent/
│   ├── core/           # Agent loop and tool schemas
│   ├── tools/          # Business logic (CRM, Enrichment, Scoring)
│   └── config.py       # OpenAI client configuration
├── main.py             # Entry point with test scenarios
├── requirements.txt    # Project dependencies
└── .env.example        # Template for environment variables
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/samirarya/ai_projects.git
cd ai_projects
```

### 2. Install Dependencies
It is recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy the example environment file and add your OpenAI API key:
```bash
cp .env.example .env
```
Edit `.env` and replace `your_api_key_here` with your actual OpenAI API key.

## Usage

Run the main script to see the agent in action with pre-configured scenarios:
```bash
python main.py
```

## How it Works

The agent follows a **Think → Act → Observe** loop:
1. **Think**: The LLM analyzes the user's request and determines which tool to call.
2. **Act**: The Python code executes the requested function (e.g., `lookup_domain_info`).
3. **Observe**: The result is fed back to the LLM to inform its next decision or final summary.
