class Agent:
    def __init__(self, name, description, tasks, goals):
        self.name = name
        self.description = description
        self.tasks = tasks
        self.goals = goals
        self.api_calls = 0

    def introduce(self):
        return f"Hello, I am {self.name}. {self.description}"

    def display_tasks(self):
        return f"My tasks include: {', '.join(self.tasks)}."

    def display_goals(self):
        return f"My goals are: {', '.join(self.goals)}."

    def increment_api_calls(self):
        self.api_calls += 1
        if self.api_calls > 10:
            raise Exception(f"{self.name} has exceeded the API call limit.")

# Example usage
if __name__ == "__main__":
    agent = Agent(
        name="Custom AI Agent",
        description="I am designed to assist with data extraction and processing.",
        tasks=["Extract data from web", "Process extracted data", "Provide insights"],
        goals=["Improve data accuracy", "Enhance processing speed", "Increase user satisfaction"]
    )
    print(agent.introduce())
    print(agent.display_tasks())
    print(agent.display_goals())
