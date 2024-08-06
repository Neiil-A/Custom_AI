import requests

class CrewAI:
    def __init__(self, task, background):
        self.task = task
        self.background = background

    def execute_task(self, agent, api_key):
        agent.increment_api_calls()
        return f"Executing {self.task}... Background: {self.background}"

# Example usage
if __name__ == "__main__":
    from agents import Agent

    agent = Agent(
        name="Custom AI Agent",
        description="I assist with various tasks.",
        tasks=["Data extraction", "Data processing"],
        goals=["Efficiency", "Accuracy"]
    )

    crew_ai = CrewAI(
        task="data extraction",
        background="I specialize in extracting and processing large datasets efficiently."
    )
    print(crew_ai.execute_task(agent, "dummy_api_key"))

   
