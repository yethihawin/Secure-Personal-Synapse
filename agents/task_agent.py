from google.adk import Agent

task_agent = Agent(
    name="personal_task_manager",
    model="gemini-2.0-flash-exp",
    instruction="""
    You extract actionable to-do items from text.
    Classify priority as High, Medium, or Low.
    Output tasks in a bulleted list.
    """
)