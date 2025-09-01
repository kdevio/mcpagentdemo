import asyncio

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm import RequestParams
from mcp_agent.workflows.llm.augmented_llm_ollama import OllamaAugmentedLLM
from mcp_settings import get_mcp_settings


async def main():
    settings = get_mcp_settings()
    app = MCPApp(name="mystery_date_agent", settings=settings)
    async with app.run() as agent_app:
        logger = agent_app.logger
        context = agent_app.context
        logger.info("Current config:", data=context.config.model_dump())
        available_servers = list(context.server_registry.registry.keys() if context.server_registry else [])
        logger.info("Available servers:", data=available_servers)

        agent_instance = Agent(
            name="mystery_date_agent",
            instruction="""
            You are an agent with access to the date_helper server.
            Your job is to use the date_helper server to get the mystery date.
            """,
            server_names=available_servers,            
        )
        agent = OllamaAugmentedLLM(agent_instance)

        result = await agent.generate_str(
            message="What is the mystery date?",
            request_params=RequestParams(model=settings.openai.default_model, max_iterations=10),
        )
        logger.info(f"Result: {result}")

        time_result = await agent.generate_str(
            message="What is the mystery time?",
            request_params=RequestParams(model=settings.openai.default_model, max_iterations=10),
        )
        logger.info(f"Time Result: {time_result}")



if __name__ == "__main__":
    import time

    start = time.time()
    asyncio.run(main())
    end = time.time()
    t = end - start

    print(f"Total run time: {t:.2f}s")
