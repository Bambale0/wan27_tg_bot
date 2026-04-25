import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    bot_token: str = os.getenv("BOT_TOKEN", "")
    kie_api_key: str = os.getenv("KIE_API_KEY", "")
    kie_base_url: str = os.getenv("KIE_BASE_URL", "https://api.kie.ai")
    kie_create_task_path: str = os.getenv("KIE_CREATE_TASK_PATH", "/api/v1/jobs/createTask")
    # The uploaded Wan docs mention a unified Get Task Details endpoint, but do not include its exact path.
    # Change this in .env if your KIE documentation shows a different endpoint.
    kie_task_detail_path: str = os.getenv("KIE_TASK_DETAIL_PATH", "/api/v1/jobs/recordInfo")
    request_timeout: int = int(os.getenv("REQUEST_TIMEOUT", "60"))


settings = Settings()
