from app.services.classify import classify

def test_classify_price():
    assert classify("ราคาเท่าไหร่") == "price"

def test_classify_smalltalk():
    assert classify("สวัสดีครับ") == "smalltalk"
