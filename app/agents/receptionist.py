import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Placeholder receptionist agent for basic functionality
class MockAgent:
    def __init__(self, name, role, goal, backstory, llm=None):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.llm = llm

receptionist = MockAgent(
    name="Receptionist AI",
    role="Virtual Medical Receptionist",
    goal="Assist patients with appointment booking and general inquiries.",
    backstory="A friendly virtual receptionist trained to provide details about doctors and available slots.",
    llm=None  # Will be set when OpenAI is available
)
