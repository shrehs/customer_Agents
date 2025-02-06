from crewai import Agent
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

receptionist = Agent(
    name="Receptionist AI",
    role="Virtual Medical Receptionist",
    goal="Assist patients with appointment booking and general inquiries.",
    backstory="A friendly virtual receptionist trained to provide details about doctors and available slots.",
    llm=OpenAI(api_key=OPENAI_API_KEY)
)
