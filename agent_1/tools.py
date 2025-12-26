import os

from crewai_tools import YoutubeChannelSearchTool
from crewai_tools.rag.data_types import DataType

os.environ.setdefault("EMBEDDINGS_OLLAMA_MODEL_NAME", "nomic-embed-text:v1.5")
os.environ.setdefault("EMBEDDINGS_OLLAMA_URL", "http://localhost:11434/api/embeddings")
os.environ.setdefault("LLM_OLLAMA_MODEL_NAME", "llama3.2:latest")
os.environ.setdefault("LLM_OLLAMA_URL", "http://localhost:11434")

youtube_channel_tool = YoutubeChannelSearchTool(
    config=dict(
        vectordb=dict(
            provider="chromadb",
            config=dict(),
        ),
        embedding_model=dict(
            provider="ollama",
            config=dict(
                url="http://localhost:11434/api/embeddings",
                model="nomic-embed-text:v1.5",
                task_type="retrieval_document",
            ),
        ),
        llm=dict(
            provider="ollama",
            config=dict(
                base_url="http://localhost:11434",
                model="llama3.2:latest",
            ),
        ),
    ),
)

try:
    youtube_channel_tool.add(
        "https://www.youtube.com/channel/UCNAf1k0yIjyGu3k9BwAg3lg",
        data_type=DataType.YOUTUBE_CHANNEL,
    )
except Exception:
    pass
