# Placeholder for scheduler agent
class MockAgent:
    def __init__(self, name, role, goal, backstory):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory

scheduler = MockAgent(
    name="Scheduler AI",
    role="Appointment Scheduler",
    goal="Find available slots and confirm appointments.",
    backstory="Handles scheduling tasks, ensuring smooth booking without conflicts."
)