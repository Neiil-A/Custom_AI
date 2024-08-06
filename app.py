# app.py
import os

# Ensure the install_path directory exists
install_path = "/mount/admin/install_path"
if not os.path.exists(install_path):
    os.makedirs(install_path)

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

import streamlit as st
from tasks import ContentGenerationTasks
from agents import ContentGenerationAgents
from tools import ExtractionTools
from crewAi import Crew, Process  # Assuming Crew and Process are defined in crewAi.py

def main():
    st.title("Content Generation Crew")
    st.write('---------------------------------')

    content_prompt = st.text_input("Please provide a prompt for the new writing content you would like to be generated, specifying type of content (blogpost, LinkedIn post, etc.), and any specific word count if you would like:")

    if st.button("Generate Content"):
        if content_prompt:
            context_file = ExtractionTools.extract_context_from_web(content_prompt)
            reference_db = ExtractionTools.generate_reference_db(content_prompt)

            tasks = ContentGenerationTasks()
            agents = ContentGenerationAgents()

            extraction_agent = agents.extraction_agent()
            prompt_analyst_agent = agents.prompt_analyst_agent()
            researcher_agent = agents.researcher_agent()
            writer_agent = agents.writer_agent()
            humanizer_agent = agents.humanizer_agent()
            reliability_agent = agents.reliability_agent()
            security_agent = agents.security_agent()

            extraction_task = tasks.extraction_task(extraction_agent, context_file, reference_db)
            analyze_prompt_task = tasks.analyze_prompt_task(prompt_analyst_agent, content_prompt, reference_db)
            research_task = tasks.research_task(researcher_agent, reference_db)
            writer_task = tasks.writer_task(writer_agent, reference_db)
            humanizer_task = tasks.humanizer_task(humanizer_agent, reference_db)
            reliability_task = tasks.reliability_task(reliability_agent)
            security_task = tasks.security_task(security_agent)

            research_task.context = [analyze_prompt_task]
            writer_task.context = [extraction_task, analyze_prompt_task, research_task]
            humanizer_task.context = [writer_task]
            reliability_task.context = [research_task]
            security_task.context = [humanizer_task]

            content_generation_crew = Crew(
                agents=[
                    extraction_agent,
                    prompt_analyst_agent,
                    researcher_agent,
                    writer_agent,
                    humanizer_agent,
                    reliability_agent,
                    security_agent
                ],
                tasks=[
                    extraction_task,
                    analyze_prompt_task,
                    research_task,
                    writer_task,
                    humanizer_task,
                    reliability_task,
                    security_task
                ],
                process=Process.parallel  # Execute tasks in parallel
            )

            result = content_generation_crew.kickoff()
            output = humanizer_task.output.raw

            st.write(output)
        else:
            st.error("Please provide a content prompt.")

if __name__ == "__main__":
    main()
