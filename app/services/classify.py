# app/services/classify.py
from __future__ import annotations
from typing import Literal, Tuple
from .retrieve import get_faq_answer, get_product_info

Intent = Literal["product", "faq", "payment", "warranty", "unknown"]

PAYMENT_HINTS = ("โอน", "ชำระ", "ผ่อน", "บัตร", "เครดิต", "พร้อมเพย์", "ปลายทาง", "มัดจำ")
WARRANTY_HINTS = ("ประกัน", "เคลม", "ซ่อม", "ศูนย์บริการ", "รับประกัน", "เงื่อนไขประกัน")

def classify_intent(message: str) -> Tuple[Intent, str]:
    """
    คืน (intent, hint) โดยพยายามอิงข้อมูลในชีทเป็นหลัก
    - ถ้า FAQ หรือ สินค้าตรง → ตีเป็นหมวดนั้น
    - ถ้าพบคำใบ้การชำระเงิน/ประกัน → ชี้ intent ตามคีย์เวิร์ด (fallback แบบปลอดภัย)
    """
    q = (message or "").strip()
    ql = q.lower()

    # สินค้า
    if get_product_info(q):
        return "product", "product_by_alias"

    # FAQ
    if get_faq_answer(q):
        return "faq", "faq_by_keyword"

    # Payment / Warranty จากคำใบ้ (ไม่มีพึ่งชีทก็ไม่ error)
    if any(k in ql for k in PAYMENT_HINTS):
        return "payment", "payment_hint"
    if any(k in ql for k in WARRANTY_HINTS):
        return "warranty", "warranty_hint"

    return "unknown", "no_match"
