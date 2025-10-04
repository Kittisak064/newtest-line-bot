import pandas as pd
from app.config import settings

def build_intent_dict():
    path = settings.faq_excel_path
    try:
        # FAQ Keywords
        faq_df = pd.read_excel(path, sheet_name="FAQ")
        faq_dict = {}
        if "คีย์เวิร์ด" in faq_df.columns and "คำตอบ" in faq_df.columns:
            for _, row in faq_df.iterrows():
                if row["คีย์เวิร์ด"]:
                    for kw in str(row["คีย์เวิร์ด"]).split(","):
                        faq_dict[kw.strip()] = ("faq", row["คำตอบ"])
        # Product Alias
        prod_df = pd.read_excel(path, sheet_name="ข้อมูลสินค้าและราคา")
        if "ชื่อสินค้าที่มักถูกเรียก" in prod_df.columns:
            for _, row in prod_df.iterrows():
                alias = str(row["ชื่อสินค้าที่มักถูกเรียก"])
                if alias and alias != "nan":
                    for kw in alias.split(","):
                        faq_dict[kw.strip()] = ("product", row.to_dict())
        return faq_dict
    except Exception as e:
        print("Error building intent dict:", e)
        return {}

INTENT_DICT = build_intent_dict()

def classify(text: str):
    t = text.lower()
    for kw, val in INTENT_DICT.items():
        if kw.lower() in t:
            return val
    # Generic fallback
    if "ราคา" in t:
        return ("product", None)
    if "ประกัน" in t:
        return ("warranty", None)
    if "ชำระ" in t or "โอน" in t:
        return ("payment", None)
    return ("unknown", None)
