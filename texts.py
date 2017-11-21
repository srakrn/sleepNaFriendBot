import random

texts = [
    'ไม่หลับไม่นอนเหรอ',
    'ระวังตื่นบ่ายสามนาจา',
    'ไข่ฝากความคิดถึงมาให้',
    'จะให้ชิไบไปม.คนเดียวจริงๆ เหรอ',
    'เราเขียนบอทแล้ว รล.ล่ะเขียน OOP ยัง',
    'อิอิ นอนได้แล้วนะ เดี๋ยวตอนสอบไม่ตื่น',
    'ชิไบฝากบอกว่านอนคนเดียวเหงามาก',
    'ถ้าทวีคไล่ไปนอนจะนอนไหม',
    'บอกว่าจะตื่นแล้วอ่ะ ถ้าเล่นเยอะระวังไม่ตื่นนะ',
    'จ่าแทนเขียนบอทนี้ให้รล.ไปนอน ถ้ารล.ไม่นอนจ่าแทนเสียจัยนะ',
    '( ͡° ͜ʖ ͡°) รูปหล่อ ลึกลับล้ำโลกลีบลูบราเรือรบหลวง',
    'ยัง ยังอีก ยังจะเปิดฟิคใหม่อีกหรอ',
    'ถ้าไม่นอนเดี๋ยว underpants gnome มาขโมยกกน.นะ',
    'People are dying. The fault is our own. You can do lots of damage when you\'re on your phone',
    'Put it down. Don\'t be on your phone while being President',
    'Oh God! Another tweet from the President',
    'Omae wa... mou shindeiru!',
    'But Ryolen, we don\'t want you to stay up late',
    'Daddy is coming for you.',
    'YOU ARE GROUNDED!',
    'ถ้ายังไม่นอน ชิไบจะละเมออัดแล้วนะ',
    'WHAT WHAT WHAAAT?',
    'Our kids won\'t go to sleep? BLAME CANADA!',
    'I\'ve got you in my sights',
    'หลับเถิดชาวไทย อย่ามัวแต่ไปลุ่มหลง',
    'ไป! ไป!! ไปนอนเดี๋ยวนี้ซะเถอะที่รัก (ไม่งั้น)ฉันจะลงโทษเธอ!!!',
    'If Craig was here, he would go to sleep too.',
    'Are you there Ryolen? It\'s me, your best friend :)',
    'Yaranaika? ( ͡° ͜ʖ ͡°)'
]

def get_text():
    text = texts[random.randint(0, len(texts)-1)]
    return text + text[-1]*random.randint(0, 10)
