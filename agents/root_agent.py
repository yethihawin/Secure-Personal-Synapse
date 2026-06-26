from google.adk import Agent

from agents.schedule_agent import schedule_agent
from agents.task_agent import task_agent

root_agent = Agent(
    name="secure_personal_synapse",
    model="gemini-2.0-flash-exp",
    instruction="""
    You are a master orchestrator.

    If input contains dates or times,
    use schedule_agent.

    If input contains tasks,
    use task_agent.

    Produce a clear organized response.
    """,
    sub_agents=[
        schedule_agent,
        task_agent
    ]
)