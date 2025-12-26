# YouTube Research Agent

A CrewAI agent that researches YouTube channels and generates blog posts based on video content, specifically focused on football-related topics.

## Overview

This agent uses CrewAI to create a multi-agent system that:
1. **Researches** relevant YouTube videos on a given topic
2. **Writes** comprehensive blog posts based on the video content

## Features

- 🔍 **YouTube Channel Search**: Searches and indexes YouTube channel content
- 📝 **Blog Post Generation**: Creates well-structured blog posts from video transcripts
- ⚽ **Football-Focused**: Specialized in football matches, analysis, and predictions
- 🧠 **Memory & Caching**: Agents maintain context and cache results for efficiency
- 🔄 **Sequential Processing**: Tasks execute in a logical sequence

## Agents

### Blog Research Agent
- **Role**: Blog researcher from YouTube videos
- **Goal**: Get relevant videos on the topic from YouTube channels
- **Expertise**: Football, football matches, analysis, and predictions

### Blog Writer Agent
- **Role**: Blog writer from YouTube videos
- **Goal**: Write blog posts on the topic from YouTube videos
- **Expertise**: Writing blog posts about football-related content

## Files

- `agents.py` - Defines the research and writer agents
- `tasks.py` - Defines the research and writing tasks
- `tools.py` - Configures the YouTube channel search tool
- `crew.py` - Sets up and runs the crew

## Prerequisites

- Python 3.11+
- Ollama installed and running locally
- Required models:
  - `llama3.2:latest` (for LLM)
  - `nomic-embed-text:v1.5` (for embeddings)

## Setup

1. Install dependencies:
```bash
pip install -r ../requirement.txt
```

2. Ensure Ollama is running:
```bash
ollama serve
```

3. Pull required models:
```bash
ollama pull llama3.2:latest
ollama pull nomic-embed-text:v1.5
```

4. Configure environment variables (if needed):
```bash
# Create a .env file in the project root
EMBEDDINGS_OLLAMA_MODEL_NAME=nomic-embed-text:v1.5
EMBEDDINGS_OLLAMA_URL=http://localhost:11434/api/embeddings
LLM_OLLAMA_MODEL_NAME=llama3.2:latest
LLM_OLLAMA_URL=http://localhost:11434
```

## Usage

Run the crew:

```python
python crew.py
```

The agent will:
1. Search for relevant YouTube videos on the specified topic
2. Generate a blog post based on the video content
3. Save the output to `blog_post.md`

## Configuration

The YouTube channel tool is pre-configured to search:
- Channel: `https://www.youtube.com/channel/UCNAf1k0yIjyGu3k9BwAg3lg`

You can modify the channel URL in `tools.py` to search different channels.

## Output

The generated blog post will be saved to `blog_post.md` in the current directory.

