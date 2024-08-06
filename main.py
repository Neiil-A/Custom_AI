# Somehow, I may have made a RAG begginer-level chatbot thingy...?
import os
from dotenv import load_dotenv
from tasks.content_generation_tasks import ContentGenerationTasks
from agents.content_generation_agents import ContentGenerationAgents
from tools.extraction_tools import ExtractionTools

def main():
    # Load environment variables from a .env file
    load_dotenv()

    print("## Welcome to the Content Generation Crew")
    print('---------------------------------')

    # Prompt the user for content generation details
    content_prompt = input("Please provide a prompt for the new writing content you would like to be generated, specifying type of content (blogpost, LinkedIn post, etc.), and any specific word count if you would like: \n")

    # Automatically handle context extraction and reference database inclusion
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

    # Display the generated content
    print(output)

if __name__ == "__main__":
    main()



