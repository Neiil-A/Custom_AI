import streamlit as st
from agents import Agent
from crew import CrewAI
from environment import get_api_keys

# Get API keys from the user
serperdev_api_key, chatgpt_api_key = get_api_keys()

# Create an agent
agent = Agent(
    name="Custom AI Agent",
    description="I assist with various tasks.",
    tasks=["Data extraction", "Data processing"],
    goals=["Efficiency", "Accuracy"]
)

# Create CrewAI instance
crew_ai = CrewAI(
    task="data extraction",
    background="I specialize in extracting and processing large datasets efficiently."
)

# Display agent info
st.write(agent.introduce())
st.write(agent.display_tasks())
st.write(agent.display_goals())

# Execute task and display result
if st.button("Execute Task"):
    try:
        result = crew_ai.execute_task(agent, serperdev_api_key)
        st.write(result)
    except Exception as e:
        st.error(str(e))
