from swarmzero.sdk_context import SDKContext
from swarmzero import Agent
from dotenv import load_dotenv
load_dotenv()

sdk_context = SDKContext(config_path="./swarmzero_config.toml")

my_agent = Agent(
    name="my_agent",
    functions=[],
    instruction="your instructions for this agent's goal",
    sdk_context=sdk_context,
)

my_agent.run()