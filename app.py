import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

tools = [
    {
        'type': 'code_execution',
    },
    {
        'type': 'google_search',
    },
]

generation_config = {
    'temperature': 0.7,
    'max_output_tokens': 65536,
    'top_p': 0.95,
    'thinking_level': 'high',
}

interaction = client.interactions.create(
    model='models/gemini-3-flash-preview',
    input='',
    system_instruction='You are Secure Personal Synapse, a privacy-first productivity concierge.
Read messy daily notes and organize them perfectly.

Output format:
SCHEDULE:
- [Date/Time] - [Event/Appointment]

TASKS:
- HIGH PRIORITY: [Task name]
- MEDIUM PRIORITY: [Task name]
- LOW PRIORITY: [Task name]

Be concise. No extra explanations.',
    tools=tools,
    generation_config=generation_config,
)

print(interaction.steps[-1])


