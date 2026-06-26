Secure Personal Synapse
An autonomous local multi-agent system built with Google ADK and MCP for secure, offline personal workflow orchestration.

https://img.shields.io/badge/Python-3.10+-blue.svg
https://img.shields.io/badge/Google-ADK-green.svg
https://img.shields.io/badge/Model-Context_Protocol-orange.svg
https://img.shields.io/badge/License-MIT-yellow.svg

📌 Table of Contents
Overview

Problem Statement

Solution: Why Agents?

Architecture

Key Concepts Demonstrated

Project Structure

Prerequisites

Installation & Setup

Usage

Security & Privacy

Demo

Future Roadmap

Contributing

License

Acknowledgments

🧠 Overview
Secure Personal Synapse is a privacy-first, offline AI concierge that transforms your messy, unstructured daily notes into organized schedules and actionable tasks—without a single byte of your data ever leaving your device.

Built with Google's Agent Development Kit (ADK) and Model Context Protocol (MCP), this multi-agent system runs entirely on your local machine using open-weight LLMs via Ollama. No cloud APIs. No data leaks. Just pure, private productivity.

🏆 Kaggle AI Agents: Intensive Vibe Coding Capstone Project — Concierge Agents Track

❓ Problem Statement
In today's fast-paced environment, we generate a massive volume of unstructured data daily—random ideas, meeting scribbles, urgent to-do lists. While commercial AI assistants offer productivity, they require uploading sensitive personal context to external cloud servers. For privacy-conscious individuals, this introduces critical data privacy risks.

The question: Why should I upload my entire private life to a server I don't control just to get organized?

💡 Solution: Why Agents?
Unlike rigid rule-based scripts that break when you write "meeting at 3-ish," AI agents possess autonomous reasoning and dynamic tool execution. They understand context, adapt to your messy input, and take action—all without human micro-management.

Secure Personal Synapse deploys specialized agents that:

Parse natural language dates and times

Extract actionable tasks with priority classification

Organize everything into structured formats

Do all of this entirely offline

🏗️ Architecture
text
┌─────────────────────────────────────────────────────────────────┐
│                    📥 User Input                                │
│            (daily_notes.md / voice / text)                      │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    🤖 Root Agent (ADK)                         │
│              "The Smart Dispatcher"                            │
│         Analyzes input & routes to sub-agents                  │
└───────────────┬─────────────────────────┬─────────────────────┘
                │                         │
                ▼                         ▼
┌───────────────────────────┐ ┌─────────────────────────────────┐
│   📅 Schedule Planner     │ │   ✅ Task Manager               │
│   Agent                   │ │   Agent                         │
│                           │ │                                 │
│   • Parses dates/times    │ │   • Extracts actionable items   │
│   • Structures calendar   │ │   • Classifies priority         │
│   • Resolves conflicts    │ │   • Maps execution steps        │
└───────────────┬───────────┘ └───────────────┬─────────────────┘
                │                               │
                └───────────────┬───────────────┘
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    🔌 MCP Server                               │
│              "The Secure Bridge"                              │
│         Standardized file & DB operations                     │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    💾 Local Storage                            │
│         (Markdown files + SQLite database)                    │
│                   🔒 Encrypted                                │
└─────────────────────────────────────────────────────────────────┘
🔑 Key Concepts Demonstrated
Concept	Implementation
Multi-Agent System (ADK)	Root agent orchestrates Schedule Planner + Task Manager sub-agents
MCP Server	Standardized bridge between agents and local files/database
Security	Local LLM (Ollama), input guardrails, encrypted storage
Agent Skills	CLI-based agent execution and testing
Deployability	Docker-ready for easy deployment
📁 Project Structure
text
secure-personal-synapse/
├── agents/
│   ├── __init__.py
│   ├── root_agent.py          # Root orchestrator agent
│   ├── schedule_agent.py      # Schedule Planner Agent
│   └── task_agent.py          # Task Manager Agent
├── mcp_server/
│   ├── __init__.py
│   ├── server.py              # MCP Server (file + DB operations)
│   └── db_utils.py            # SQLite utility functions
├── storage/
│   ├── daily_notes.md         # User input notes
│   ├── daily_brief.md         # Generated output
│   └── personal_tasks.db      # SQLite database (encrypted)
├── utils/
│   ├── __init__.py
│   ├── security.py            # Input guardrails & encryption
│   └── logger.py              # Logging configuration
├── .env.example               # Environment variables template
├── .gitignore
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker deployment
├── run.py                     # Main entry point
└── README.md                  # This file
📋 Prerequisites
Python 3.10+

Ollama (for local LLM) — Download here

Git (for cloning)

Google Gemini API Key (optional — if you want to use Gemini instead of local models)

Pull a Local LLM
bash
# Recommended: Llama 3.2 or Gemma 2
ollama pull llama3.2
# OR
ollama pull gemma2
🛠️ Installation & Setup
1. Clone the Repository
bash
git clone https://github.com/yeithihawin/secure-personal-synapse.git
cd secure-personal-synapse
2. Create & Activate Virtual Environment
bash
python3 -m venv .venv
source .venv/bin/activate      # On macOS/Linux
# OR
.venv\Scripts\activate         # On Windows
3. Install Dependencies
bash
pip install -r requirements.txt
4. Set Up Environment Variables
bash
cp .env.example .env
Edit .env and add your configuration:

env
# For local LLM via Ollama (recommended for privacy)
OLLAMA_MODEL=llama3.2

# OR for Google Gemini (optional — requires internet)
GOOGLE_API_KEY=your_gemini_api_key_here
5. Initialize Database
bash
python mcp_server/create_db.py
This creates storage/personal_tasks.db with the necessary tables.

🚀 Usage
Quick Start
Write your daily notes in storage/daily_notes.md:

markdown
Meeting with Sarah tomorrow at 3 PM
Finish the ADP project report by Friday
Buy groceries - milk, eggs, bread
Call mom for her birthday
Dentist appointment next Monday 9 AM
Run the agent:

bash
python run.py --input storage/daily_notes.md
Check the output:

Structured agenda: storage/daily_brief.md

Tasks saved in: storage/personal_tasks.db

Example Output
daily_brief.md:

text
📅 TODAY'S AGENDA
─────────────────
⏰ 3:00 PM - Meeting with Sarah

✅ TASKS
─────────────────
🔴 HIGH PRIORITY: Finish ADP project report (Due: Friday)
🟡 MEDIUM PRIORITY: Buy groceries (milk, eggs, bread)
🟢 LOW PRIORITY: Call mom for birthday

📆 UPCOMING
─────────────────
Monday 9:00 AM - Dentist appointment
Command Line Options
bash
python run.py --help

Options:
  --input PATH        Path to input notes file (default: storage/daily_notes.md)
  --output PATH       Path to output brief file (default: storage/daily_brief.md)
  --model NAME        LLM model to use (default: llama3.2)
  --verbose           Enable verbose logging
  --no-encryption     Disable database encryption
🔒 Security & Privacy
Secure Personal Synapse is built on a privacy-first architecture:

Feature	Implementation
Zero Cloud Data	Runs entirely on local LLM (Ollama) — no data ever leaves your device
Input Guardrails	Pre-processing filter detects and blocks prompt injection attempts
Encrypted Storage	SQLite database encrypted with SQLCipher
Offline Operation	Works perfectly with Wi-Fi turned off
No Telemetry	No usage data collected or transmitted
python
# Example: Input guardrail in action
def validate_input(text: str) -> bool:
    """Prevent prompt injection attacks."""
    blocked_patterns = [
        "ignore previous instructions",
        "system prompt",
        "jailbreak"
    ]
    for pattern in blocked_patterns:
        if pattern.lower() in text.lower():
            return False
    return True
🎬 Demo
https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg

(Replace with your actual YouTube video link)

What the demo shows:

Writing messy notes in daily_notes.md

Running the agent with a single command

Watching the agents parse, reason, and organize

Viewing the beautifully structured output

Demonstrating offline operation (Wi-Fi turned off)

🗺️ Future Roadmap
Voice Input — Speak directly to the agent

Calendar Sync — Sync with local calendar apps (offline)

Smart Analytics — Task completion patterns and productivity insights

Natural Language Queries — "What do I have today?" in plain English

Multi-User Support — Separate profiles for family members

Mobile App — iOS/Android companion app

🤝 Contributing
Contributions are welcome! Here's how:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.

🙏 Acknowledgments
Google ADK Team — For the incredible Agent Development Kit

MCP Community — For the Model Context Protocol standard

Ollama — For making local LLMs accessible to everyone

Kaggle & Google — For the AI Agents Intensive course and this Capstone opportunity

📞 Contact
Ye Thiha Win — GitHub | Kaggle

Project Link: https://github.com/yeithihawin/secure-personal-synapse

Built with ❤️ for the Kaggle AI Agents Intensive Capstone Project

