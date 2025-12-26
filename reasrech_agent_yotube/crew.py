from crewai import Crew, Process
from tasks import blog_research_task, blog_writer_task
from agents import blog_research_agent, blog_writer_agent
from tools import youtube_channel_tool

crew = Crew(
    agents=[blog_research_agent, blog_writer_agent],
    tasks=[blog_research_task, blog_writer_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    verbose=True,
    share_crew=True,
)

result = crew.kickoff(
    input="🚨 FREE MOVE TO REAL MADRID? SZOBOSZLAI DEAL! MESSI AND GALATASARAY, LEWANDOWSKI, ENDRICK…"
)
print(result)