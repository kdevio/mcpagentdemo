from mcp_agent.config import (
    MCPServerSettings,
    MCPSettings,
    OpenAISettings,
    Settings
)
import sys


DEFAULT_LLM = "llama3.3:latest"


def get_mcp_server_settings() -> dict:
    return {
        "date_helper": MCPServerSettings(
            name="date_helper",
            command=sys.executable,
            args=["mcp_date_server.py"],
            env=None,
        )
    }


def get_mcp_settings(model: str = DEFAULT_LLM) -> Settings:
    openai_settings = OpenAISettings(
        base_url="http://localhost:11434/v1",
        default_model=model,
        api_key="none",
    )

    mcp_settings = Settings(
        execution_engine="asyncio",
        mcp=MCPSettings(servers=get_mcp_server_settings()),
        openai=openai_settings,
    )
    return mcp_settings
