import os
import streamlit as st
from crewai import Crew, Process
from tasks.content_generation_tasks import ContentGenerationTasks
from agents.content_generation_agents import ContentGenerationAgents
from tools.extraction_tools import ExtractionTools

class ContentGeneratorUI:
    def generate_content(self, prompt, openai_key):
        # Set OpenAI API key as an environment variable
        os.environ["OPENAI_API_KEY"] = openai_key

        content_prompt = prompt
        context_file = ExtractionTools.extract_context_from_web(content_prompt)
        reference_db = ExtractionTools.generate_reference_db(content_prompt)

        # Initialize tasks and agents
        tasks = ContentGenerationTasks()
        agents = ContentGenerationAgents()

        # Create agent instances
        extraction_agent = agents.extraction_agent()
        prompt_analyst_agent = agents.prompt_analyst_agent()
        researcher_agent = agents.researcher_agent()
        writer_agent = agents.writer_agent()
        humanizer_agent = agents.humanizer_agent()
        reliability_agent = agents.reliability_agent()
        security_agent = agents.security_agent()

        # Create task instances and set contexts
        extraction_task = tasks.extraction_task(extraction_agent, context_file, reference_db)
        analyze_prompt_task = tasks.analyze_prompt_task(prompt_analyst_agent, content_prompt, reference_db)
        research_task = tasks.research_task(researcher_agent, reference_db)
        writer_task = tasks.writer_task(writer_agent, reference_db)
        humanizer_task = tasks.humanizer_task(humanizer_agent, reference_db)
        reliability_task = tasks.reliability_task(reliability_agent)
        security_task = tasks.security_task(security_agent)

        # Define task execution order
        research_task.context = [analyze_prompt_task]
        writer_task.context = [extraction_task, analyze_prompt_task, research_task]
        humanizer_task.context = [writer_task]
        reliability_task.context = [research_task]
        security_task.context = [humanizer_task]

        # Initialize the CrewAI content generation crew
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

        # Start the content generation process
        result = content_generation_crew.kickoff()
        output = humanizer_task.output.raw

        return output

    def render(self):
        st.set_page_config(page_title="Content Generation Crew", page_icon="✍️")

        st.title("Content Generation Crew")

        # Get user input for content prompt and OpenAI API key
        content_prompt = st.text_input("Enter the content prompt:")
        openai_key = st.text_input("Enter your OpenAI API key:", type="password")

        if st.button("Generate Content"):
            if content_prompt and openai_key:
                with st.spinner("Generating content..."):
                    result = self.generate_content(content_prompt, openai_key)
                    st.success("Content generated successfully!")
                    st.text_area("Generated Content", value=result, height=400)
            else:
                st.error("Please provide both a content prompt and OpenAI API key.")

if __name__ == "__main__":
    ContentGeneratorUI().render()
