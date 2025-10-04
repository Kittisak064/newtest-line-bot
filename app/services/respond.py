from app.services import classify, llm
from app.schemas.response import BotResponse

async def generate_reply(text: str) -> BotResponse:
    intent = classify.classify(text)

    if intent in ("abuse","handover"):
        return BotResponse(
            text="หนูขออภัยค่ะ 🙏 หากต้องการให้แอดมินช่วย กดปุ่มได้เลย",
            handover=True,
            quick_replies=["ขอคุยกับแอดมิน","ดูสินค้า"]
        )
    kb_answer = f"คำตอบตัวอย่างสำหรับ intent: {intent}" if intent!="unknown" else None
    final = await llm.draft_reply(text, kb_answer)
    return BotResponse(text=final, handover=False, quick_replies=["ดูสินค้า","ขอคุยกับแอดมิน"])
