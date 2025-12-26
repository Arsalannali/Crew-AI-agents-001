# Financial Analysis Agent

A comprehensive CrewAI multi-agent system for financial market analysis, trading strategy development, and risk assessment.

## Overview

This agent uses CrewAI to create a sophisticated financial analysis system with five specialized agents that work together to:
1. **Analyze** market data in real-time
2. **Develop** trading strategies
3. **Plan** trade execution
4. **Assess** risks
5. **Generate** comprehensive reports

## Features

- 📊 **Real-time Market Analysis**: Monitor and analyze market data using statistical modeling
- 💼 **Trading Strategy Development**: Create and test various trading strategies
- ⚡ **Trade Execution Planning**: Optimize trade timing and execution methods
- 🛡️ **Risk Management**: Comprehensive risk assessment and mitigation strategies
- 📝 **Automated Reporting**: Generate detailed financial analysis reports
- 🔍 **Web Search & Scraping**: Access real-time financial data and news

## Agents

### 1. Data Analyst Agent
- **Role**: Data Analyst
- **Goal**: Monitor and analyze market data in real-time to identify trends and predict market movements
- **Expertise**: Statistical modeling, machine learning, financial market analysis

### 2. Trading Strategy Developer Agent
- **Role**: Trading Strategy Developer
- **Goal**: Develop and test various trading strategies based on data insights
- **Expertise**: Quantitative analysis, strategy development, performance evaluation

### 3. Trade Advisor Agent
- **Role**: Trade Advisor
- **Goal**: Suggest optimal trade execution strategies
- **Expertise**: Trade timing, price analysis, execution logistics

### 4. Risk Advisor Agent
- **Role**: Risk Advisor
- **Goal**: Evaluate and provide insights on trading risks
- **Expertise**: Risk assessment models, market dynamics, risk mitigation

### 5. Report Writer Agent
- **Role**: Report Writer
- **Goal**: Write comprehensive reports summarizing all analysis
- **Expertise**: Financial writing, data synthesis, report generation

## Files

- `financial_analysis.ipynb` - Jupyter notebook containing all agents, tasks, and crew configuration

## Prerequisites

- Python 3.11+
- Ollama installed and running locally
- Serper API key (for web search)
- Required models:
  - `llama3.2:latest` (for LLM)

## Setup

1. Install dependencies:
```bash
pip install -r ../requirement.txt
```

2. Ensure Ollama is running:
```bash
ollama serve
```

3. Pull required model:
```bash
ollama pull llama3.2:latest
```

4. Configure environment variables:
```bash
# Create a .env file in the project root
SERPER_API_KEY=your_serper_api_key_here
OLLAMA_MODEL=llama3.2:latest
OLLAMA_URL=http://localhost:11434
TEMPERATURE=0.6
```

## Usage

1. Open the Jupyter notebook:
```bash
jupyter notebook financial_analysis.ipynb
```

2. Run all cells to:
   - Initialize the LLM
   - Create all agents
   - Define tasks
   - Set up the crew

3. Execute the crew with your parameters:
```python
result = financial_trading_crew.kickoff(
    inputs={
        "stock_selection": "AAPL",  # Your stock symbol
        "risk_tolerance": "moderate",  # low, moderate, or high
        "trading_strategy_preference": "day trading"  # Your preference
    }
)
```

## Input Parameters

- **stock_selection**: Stock symbol to analyze (e.g., "AAPL", "TSLA")
- **risk_tolerance**: Risk level - "low", "moderate", or "high"
- **trading_strategy_preference**: Trading style (e.g., "day trading", "swing trading", "long-term")

## Output

The system generates a comprehensive report that includes:
- Market analysis and trends
- Trading strategy recommendations
- Trade execution plans
- Risk assessment and mitigation strategies
- Overall financial analysis summary

## Tools Used

- **SerperDevTool**: For searching financial news and market data
- **ScrapeWebsiteTool**: For extracting detailed information from financial websites

## Notes

- The agents work sequentially to ensure each step builds on the previous analysis
- All agents have access to web search and scraping tools for real-time data
- The system uses Ollama for local LLM inference, ensuring privacy and control

