from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.openai_api_key)

SYSTEM_PROMPT = (
    "คุณคือผู้ช่วยลูกค้าที่สุภาพ พูดไทยธรรมชาติ 🙂🙏✨ "
    "เรียกลูกค้าว่า 'คุณลูกค้า/คุณพี่' "
    "ห้ามสรุปยอดออเดอร์อัตโนมัติ "
    "หากไม่ทราบต้องบอกตามตรง และแนะนำให้ติดต่อแอดมิน"
)

async def draft_reply(user_text: str, kb_answer: str | None) -> str:
    content = f"ฐานข้อมูล: {kb_answer or 'ไม่มีข้อมูล'}\n\nคำถามลูกค้า: {user_text}"
    resp = client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":content}
        ],
        temperature=0.4,
        timeout=20
    )
    return resp.choices[0].message.content.strip()
