import httpx
from app.config import settings

async def push_to_admin_inbox(payload: dict):
    if not settings.admin_inbox_webhook:
        return
    async with httpx.AsyncClient(timeout=10) as client:
        await client.post(settings.admin_inbox_webhook, json=payload)
