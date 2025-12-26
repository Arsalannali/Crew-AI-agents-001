from crewai import Task
from tools import youtube_channel_tool
from agents import blog_research_agent, blog_writer_agent

blog_research_task = Task(
    agent=blog_research_agent,
    task="get the relevent video on the topic{topic} from youtube videos",
    expected_output="the relevent video on the topic{topic} from youtube videos",
    verbose=True,
    tools=[youtube_channel_tool],
)

blog_writer_task = Task(
    agent=blog_writer_agent,
    task="write a blog post on the topic{topic} from youtube videos",
    expected_output="a blog post on the topic{topic} from youtube videos",
    verbose=True,
    tools=[youtube_channel_tool],
    async_execution=False,
    output_file="blog_post.md",
)