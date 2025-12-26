# CrewAI Agents Collection

A collection of specialized AI agents built with CrewAI framework for various use cases including YouTube research, blog generation, and financial market analysis.

## 🚀 Overview

This repository contains multiple CrewAI agent implementations, each designed for specific tasks:

1. **YouTube Research Agent** - Researches YouTube channels and generates blog posts
2. **Financial Analysis Agent** - Comprehensive financial market analysis and trading strategy system

## 📁 Project Structure

```
crewAI_001/
├── reasrech_agent_yotube/      # YouTube research and blog generation agent
│   ├── agents.py               # Agent definitions
│   ├── tasks.py                # Task definitions
│   ├── tools.py                # YouTube search tool configuration
│   ├── crew.py                 # Crew setup and execution
│   └── README.md               # Agent-specific documentation
│
├── financial analysis agent/   # Financial market analysis agent
│   ├── financial_analysis.ipynb # Complete agent system in Jupyter notebook
│   └── README.md               # Agent-specific documentation
│
├── requirement.txt             # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## 🛠️ Prerequisites

Before running any of the agents, ensure you have:

- **Python 3.11+**
- **Ollama** installed and running locally
  - Download from: https://ollama.ai/
  - Required models:
    - `llama3.2:latest` (for LLM)
    - `nomic-embed-text:v1.5` (for embeddings - YouTube agent only)

- **API Keys** (for Financial Analysis Agent):
  - Serper API key: https://serper.dev/

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Arsalannali/Crew-AI-agents-001.git
cd Crew-AI-agents-001
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirement.txt
```

4. Set up Ollama:
```bash
# Start Ollama service
ollama serve

# Pull required models
ollama pull llama3.2:latest
ollama pull nomic-embed-text:v1.5  # For YouTube agent
```

5. Configure environment variables:
```bash
# Create a .env file in the project root
SERPER_API_KEY=your_serper_api_key_here  # For Financial Analysis Agent
OLLAMA_MODEL=llama3.2:latest
OLLAMA_URL=http://localhost:11434
TEMPERATURE=0.6
```

## 🤖 Agents

### 1. YouTube Research Agent

A multi-agent system that researches YouTube channels and generates blog posts, specifically focused on football-related content.

**Location**: `reasrech_agent_yotube/`

**Features**:
- YouTube channel search and indexing
- Blog post generation from video transcripts
- Football-focused content analysis
- Sequential task processing

**Quick Start**:
```bash
cd reasrech_agent_yotube
python crew.py
```

For detailed documentation, see [reasrech_agent_yotube/README.md](reasrech_agent_yotube/README.md)

### 2. Financial Analysis Agent

A comprehensive financial market analysis system with five specialized agents for market analysis, strategy development, risk assessment, and report generation.

**Location**: `financial analysis agent/`

**Features**:
- Real-time market data analysis
- Trading strategy development
- Risk assessment and management
- Automated comprehensive reporting
- Web search and data scraping

**Quick Start**:
```bash
cd "financial analysis agent"
jupyter notebook financial_analysis.ipynb
```

For detailed documentation, see [financial analysis agent/README.md](financial%20analysis%20agent/README.md)

## 📋 Dependencies

Key dependencies include:
- `crewai` - Multi-agent framework
- `crewai_tools` - Pre-built tools for agents
- `langchain-community` - LLM integrations
- `ollama` - Local LLM inference
- `python-dotenv` - Environment variable management
- `qdrant-client` - Vector database (for YouTube agent)
- `litellm` - LLM abstraction layer

See `requirement.txt` for the complete list.

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Ollama Configuration
OLLAMA_MODEL=llama3.2:latest
OLLAMA_URL=http://localhost:11434
TEMPERATURE=0.6

# Embeddings (for YouTube agent)
EMBEDDINGS_OLLAMA_MODEL_NAME=nomic-embed-text:v1.5
EMBEDDINGS_OLLAMA_URL=http://localhost:11434/api/embeddings

# API Keys
SERPER_API_KEY=your_serper_api_key_here  # For Financial Analysis Agent
```

## 🚦 Usage Examples

### YouTube Research Agent
```python
from crew import crew

result = crew.kickoff(
    input="🚨 FREE MOVE TO REAL MADRID? SZOBOSZLAI DEAL! MESSI AND GALATASARAY..."
)
print(result)
```

### Financial Analysis Agent
```python
result = financial_trading_crew.kickoff(
    inputs={
        "stock_selection": "AAPL",
        "risk_tolerance": "moderate",
        "trading_strategy_preference": "day trading"
    }
)
```

## 📝 Notes

- Both agents use **Ollama** for local LLM inference, ensuring privacy and control
- Agents support **memory** and **caching** for improved performance
- The Financial Analysis Agent requires internet access for real-time market data
- The YouTube Research Agent uses vector databases for efficient video search

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Serper API](https://serper.dev/)

## 👤 Author

**Arsalannali**

- GitHub: [@Arsalannali](https://github.com/Arsalannali)

---

⭐ If you find this project useful, please consider giving it a star!

