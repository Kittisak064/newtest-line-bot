import uvicorn, logging
from fastapi import FastAPI
from app.logging_conf import configure_logging
from app.routers import webhook_line, health

configure_logging()
log = logging.getLogger(__name__)

app = FastAPI(title="LINE Chatbot")

app.include_router(health.router, tags=["health"])
app.include_router(webhook_line.router, tags=["line"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
