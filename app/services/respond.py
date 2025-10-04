# app/services/respond.py
from app.services import classify, retrieve

async def generate_reply(user_message: str) -> str:
    """
    ตอบข้อความลูกค้าโดยอิงจาก intent + ข้อมูลในชีท
    """
    intent, detail = classify.classify_intent(user_message)

    # -----------------------------
    # 1) ถามสินค้า → ใช้ชีท 'ข้อมูลสินค้าและราคา'
    # -----------------------------
    if intent == "product":
        product_info = retrieve.get_product_info(user_message)
        if product_info:
            return f"คุณลูกค้าสนใจ {product_info['name']} ราคา {product_info['price']} บาท\nรายละเอียด: {product_info['desc']}"
        else:
            return "ขออภัยค่ะ ฟักแฟงยังไม่พบสินค้านี้ในระบบนะคะ"

    # -----------------------------
    # 2) FAQ → ใช้ชีท 'FAQ'
    # -----------------------------
    elif intent == "faq":
        faq_answer = retrieve.get_faq_answer(user_message)
        if faq_answer:
            return f"คำถามที่พบบ่อย: {faq_answer}"
        else:
            return "ฟักแฟงยังไม่มีคำตอบในหมวด FAQ สำหรับคำถามนี้ค่ะ"

    # -----------------------------
    # 3) ก่อนการขาย (Pre-Sale)
    # -----------------------------
    elif intent == "pre_sale":
        instr = retrieve.get_pre_sale_instruction()
        return f"📌 ข้อมูลก่อนการขาย:\n{instr}"

    # -----------------------------
    # 4) หลังการขาย (After-Sale)
    # -----------------------------
    elif intent == "after_sale":
        instr = retrieve.get_after_sale_instruction()
        return f"📌 ข้อมูลหลังการขาย:\n{instr}"

    # -----------------------------
    # 5) การชำระเงิน
    # -----------------------------
    elif intent == "payment":
        payment_info = retrieve.get_payment_info()
        return f"💳 ช่องทางการชำระเงิน:\n{payment_info}"

    # -----------------------------
    # 6) การรับประกัน/การเคลม
    # -----------------------------
    elif intent == "warranty":
        warranty_info = retrieve.get_warranty_info()
        return f"🛠️ ข้อมูลการรับประกัน:\n{warranty_info}"

    # -----------------------------
    # 7) ไม่ตรงกับ intent ใด ๆ
    # -----------------------------
    else:
        return "ฟักแฟงยังไม่เข้าใจคำถามนี้ค่ะ คุณลูกค้าสามารถสอบถามเรื่องสินค้า ราคา การชำระเงิน หรือการรับประกันได้นะคะ 💕"
