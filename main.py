# Somehow, I may have made a RAG begginer-level chatbot thingy...?
import os
from dotenv import load_dotenv
from crewai import Crew, Process
from tasks.content_generation_tasks import ContentGenerationTasks
from agents.content_generation_agents import ContentGenerationAgents
from tools.extraction_tools import ExtractionTools

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from tasks.content_generation_tasks import ContentGenerationTasks
from agents.content_generation_agents import ContentGenerationAgents
from tools.extraction_tools import ExtractionTools

def main():
    load_dotenv()

    print("## Welcome to my Content Generation. Do not Use at your convenience, but edit to improve it if necessary.")
    print('---------------------------------')

    content_prompt = input("Please provide a prompt for the new writing content you would like to be generated, specifying type of content and any specific word count: \n")

    # Automatically fetch context and reference database
    context_file = ExtractionTools.get_context_file(content_prompt)
    reference_db = ExtractionTools.get_reference_db(content_prompt)

    tasks = ContentGenerationTasks()
    agents = ContentGenerationAgents()

    extraction_agent = agents.extraction_agent()
    prompt_analyst_agent = agents.prompt_analyst_agent()
    researcher_agent = agents.researcher_agent()
    writer_agent = agents.writer_agent()
    humanizer_agent = agents.humanizer_agent()
    darth_vader_agent = agents.darth_vader_agent()
    security_agent = agents.security_agent()

    extraction_task = tasks.extraction_task(extraction_agent, context_file, reference_db)
    analyze_prompt_task = tasks.analyze_prompt_task(prompt_analyst_agent, content_prompt, reference_db)
    research_task = tasks.research_task(researcher_agent, reference_db)
    writer_task = tasks.writer_task(writer_agent, reference_db)
    humanizer_task = tasks.humanizer_task(humanizer_agent, reference_db)
    validate_sources_task = tasks.validate_sources_task(darth_vader_agent)
    ensure_security_task = tasks.ensure_security_task(security_agent)
  #man, ... this was supposed to be named Security, That's Tha Sound of Tha Police!

    research_task.context = [analyze_prompt_task]
    writer_task.context = [extraction_task, analyze_prompt_task, research_task]
    humanizer_task.context = [writer_task]
    validate_sources_task.context = [research_task]
    ensure_security_task.context = [validate_sources_task]

    content_generation_crew = Crew(
        agents=[
            extraction_agent,
            prompt_analyst_agent,
            researcher_agent,
            writer_agent,
            humanizer_agent,
            darth_vader_agent,
            security_agent
        ],
        tasks=[
            extraction_task,
            analyze_prompt_task,
            research_task,
            writer_task,
            humanizer_task,
            validate_sources_task,
            ensure_security_task
        ],
        process=Process.parallel
    )

    result = content_generation_crew.kickoff()
    output = humanizer_task.output.raw

    print(output)

if __name__ == "__main__":
    main()
