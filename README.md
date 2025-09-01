## MCP Agent Demo — Setup & Run

### Prerequisites
- **Python**: 3.11+
- **Ollama**: Install from [Ollama downloads](https://ollama.com/download)

### Configure your model
- In `mcp_settings.py`, set `DEFAULT_LLM` to the model you want Ollama to run.
- Pull the model into Ollama:
```bash
ollama pull <model_name>
# Example
ollama pull llama3.3:latest
```

### Start Ollama (separate terminal)
```bash
ollama serve
```

### Project setup
Use the Makefile to create a virtual environment and install dependencies:
```bash
make setup
```

Activate the environment:
```bash
source .venv/bin/activate
```

### Run the demo with the env activated if it's not already
```bash
python main.py
```