from fastapi import APIRouter, Request
from app.services.respond import generate_reply
from app.services.line_api import send_line_reply

router = APIRouter()

@router.post("/webhook/line")
async def line_webhook(req: Request):
    body = await req.json()
    events = body.get("events", [])

    for ev in events:
        if ev.get("type") == "message" and ev["message"]["type"] == "text":
            text = ev["message"]["text"]

            # เรียก AI/Google Sheet เพื่อตอบกลับ
            bot_resp = await generate_reply(text)

            # ส่งกลับ LINE (ไม่ต้องใช้ .text แล้ว)
            await send_line_reply(ev["replyToken"], bot_resp)

    return {"status": "ok"}
