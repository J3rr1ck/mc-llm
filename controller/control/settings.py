from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):

    # Agent
    agent_origin: str = "http://localhost"
    agent_port: int = 3000
    prompt_template_dir: Path = Path(__file__).parent.parent / "prompts"
    system_prompt_file: Path = Path("system_prompt.txt")

        # OpenAI Server
    openai_server_url: str = "http://localhost:1234"  # Add this line
    openai_api_key: str
    
    class Config:
        env_file = ".env"


settings = Settings()
