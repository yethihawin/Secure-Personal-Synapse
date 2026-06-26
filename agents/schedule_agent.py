from google.adk import Agent

schedule_agent = Agent(
    name="personal_schedule_planner",
    model="gemini-2.0-flash-exp",
    instruction="""
    Extract dates, times, appointments and deadlines.
    Return them in a structured format.
    """
)