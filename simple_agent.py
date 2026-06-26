import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""
    You are Secure Personal Synapse, a privacy-first productivity concierge.
    Your task is to read messy daily notes and organize them perfectly.

    Extract and structure the following:
    1. SCHEDULE: All dates, times, appointments, and deadlines.
    2. TASKS: Actionable to-do items. Classify each as HIGH, MEDIUM, or LOW priority.

    Output must be clear, well-formatted, and easy to read.
    """
)


user_input = """
Meeting with Sarah tomorrow at 3 PM.
Finish the ADP project report by this Friday.
Buy groceries - milk, eggs, bread.
Call mom for her birthday.
Dentist appointment on Monday 9 AM.
Team lunch on Wednesday at 12:30 PM.
Pay electricity bill by June 30.
Schedule a meeting with the boss next Tuesday at 10 AM.
"""

print("🔐 Secure Personal Synapse is running (Simple Version)...")
print("📥 Input:\n", user_input)
print("\n🤖 Processing with Gemini...\n")
print("-" * 50)


response = model.generate_content(user_input)

print("📋 Organized Output:\n")
print(response.text)
print("\n" + "-" * 50)
print("✅ Done! (No complex ADK errors!)")