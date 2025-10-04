from fastapi import APIRouter, Request, HTTPException
import hmac, hashlib, base64, logging, httpx
from app.config import settings
from app.services.respond import generate_reply

router = APIRouter()
log = logging.getLogger(__name__)

def verify_signature(body: bytes, signature: str) -> bool:
    mac = hmac.new(settings.line_secret.encode("utf-8"), body, hashlib.sha256).digest()
    expected = base64.b64encode(mac).decode()
    return hmac.compare_digest(expected, signature)

@router.post("/webhook/line")
async def line_webhook(request: Request):
    body = await request.body()
    sig = request.headers.get("x-line-signature","")
    if not verify_signature(body, sig):
        raise HTTPException(status_code=401, detail="Invalid signature")

    data = await request.json()
    results = []
    for ev in data.get("events", []):
        if ev.get("type")!="message" or ev["message"].get("type")!="text":
            continue
        user_id = ev["source"]["userId"]
        text = ev["message"]["text"]
        bot_resp = await generate_reply(text)
        await send_line_reply(ev["replyToken"], bot_resp.text)
        results.append({"user":user_id,"ok":True})
    return {"results":results}

async def send_line_reply(reply_token: str, text: str):
    payload = {"replyToken": reply_token, "messages":[{"type":"text","text":text}]}
    async with httpx.AsyncClient(timeout=10, headers={
        "Authorization": f"Bearer {settings.line_access_token}"
    }) as client:
        r = await client.post("https://api.line.me/v2/bot/message/reply", json=payload)
        if r.status_code >= 300:
            log.error("LINE reply error: %s %s", r.status_code, r.text)
