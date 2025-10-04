from typing import Literal

Intent = Literal["price","spec","stock","shipping","warranty","claim","smalltalk","abuse","handover","unknown"]

KEYWORDS = {
    "price":["ราคา","เท่าไหร่","กี่บาท"],
    "spec":["สเปก","รับน้ำหนัก","แรงม้า","กี่ชั้น"],
    "stock":["มีของ","พร้อมส่ง","สต็อก"],
    "shipping":["ส่ง","กี่วัน","ขนส่ง"],
    "warranty":["ประกัน","รับประกัน"],
    "claim":["เคลม","เสีย","ชำรุด","ซ่อม"],
    "smalltalk":["สวัสดี","ขอบคุณ","ครับ","ค่ะ","hello"],
    "abuse":["เหี้ย","กาก","ฟาย","fuck","shit"]
}

def classify(text: str) -> Intent:
    t = text.lower()
    for intent, kws in KEYWORDS.items():
        if any(k in t for k in kws):
            return intent  # type: ignore
    if "แอดมิน" in t or "คนจริง" in t:
        return "handover"
    return "unknown"
