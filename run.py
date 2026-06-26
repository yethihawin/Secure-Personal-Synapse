import os
from dotenv import load_dotenv
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agents.root_agent import root_agent

load_dotenv()


def main():
    print("Starting Secure Personal Synapse...")

    session_service = InMemorySessionService()

    runner = Runner(
        app_name="secure_personal_synapse",
        agent=root_agent,
        session_service=session_service,
    )

    user_input = """
    Meeting with Sarah tomorrow at 3 PM.
    Finish the ADP project report by this Friday.
    Buy groceries - milk, eggs, bread.
    Call mom for her birthday.
    """

    session_id = "session_001"
    user_id = "user_001"

    user_content = types.Content(
        role="user",
        parts=[types.Part(text=user_input)]
    )

    events = runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=user_content
    )

    for event in events:
        if event.content:
            for part in event.content.parts:
                if hasattr(part, "text") and part.text:
                    print(part.text)


if __name__ == "__main__":
    main()