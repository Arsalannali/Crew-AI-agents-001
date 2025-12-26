from crewai import Agent, LLM

from tools import youtube_channel_tool

from dotenv import load_dotenv

load_dotenv()

ollama_llm = LLM(
    model="ollama/llama3.2:latest",
    provider="ollama",
    base_url="http://localhost:11434",
    api_base="http://localhost:11434",
    temperature=0,
)

blog_research_agent = Agent(
    role="Blog researcher from youtube videos",
    goal="get the relevent video on the topic{topic} from youtube videos",
    backstory="you are expert in understanding football, football matches, analysis and predictions of football matches",
    verbose=True,
    memory=True,
    tools=[youtube_channel_tool],
    allow_delegation=True,
    llm=ollama_llm,
)

blog_writer_agent = Agent(
    role="Blog writer from youtube videos",
    goal="write a blog post on the topic{topic} from youtube videos",
    backstory="you are expert in writing blog posts on the topic of football, football matches, analysis and predictions of football matches",
    verbose=True,
    memory=True,
    tools=[youtube_channel_tool],
    allow_delegation=True,
    llm=ollama_llm,
)