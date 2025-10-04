from pydantic import BaseModel
from typing import Optional, List

class BotResponse(BaseModel):
    text: str
    handover: bool = False
    quick_replies: Optional[List[str]] = None
