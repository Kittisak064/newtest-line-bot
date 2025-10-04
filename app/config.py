import os
from pydantic import BaseModel

class Settings(BaseModel):
    app_env: str = os.getenv("APP_ENV", "dev")
    port: int = int(os.getenv("PORT", "8000"))

    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    line_secret: str = os.getenv("LINE_CHANNEL_SECRET", "")
    line_access_token: str = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "")

    admin_inbox_webhook: str = os.getenv("ADMIN_INBOX_WEBHOOK", "")

settings = Settings()
