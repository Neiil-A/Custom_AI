from crewai import Task
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

class ContentGenerationTasks:
    def extraction_task(self, agent, context_file, reference_db):
        return Task(
            description=f"Extract content from the markdown document and organize it. Context file: {context_file}, Reference DB: {reference_db}",
            expected_output="An organized file with the contents of the writing piece, including a clear title, body, etc.",
            agent=agent,
            async_execution=True
        )

    def analyze_prompt_task(self, agent, content_prompt, reference_db):
        return Task(
            description=f"Create a detailed prompt based on the user-given content prompt. Include specific queries for the researcher and guidelines for the writer. Content prompt: {content_prompt}, Reference DB: {reference_db}",
            expected_output="A detailed prompt for the researcher and writer, tailored to the user's needs.",
            agent=agent,
        )

    def research_task(self, agent, reference_db):
        return Task(
            description=f"Conduct comprehensive research on the topic using the search tool. Compile an in-depth report from the gathered information. Reference DB: {reference_db}",
            expected_output="A detailed report with key findings and a list of sources used.",
            agent=agent,
            tools=[search_tool]
        )

   
