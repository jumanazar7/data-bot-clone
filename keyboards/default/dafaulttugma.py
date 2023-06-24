from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

admin_tugma = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📥 Yangi Fan"),KeyboardButton(text="📥 Yangi Ustoz")],
        [KeyboardButton(text="❌ Fani o'chirish"),KeyboardButton(text="❌ Ustozni O'chirish")],
        [KeyboardButton(text="👤 Barcha Foydalanuchilar"),KeyboardButton("🗣 Reklama yubor")],
        [KeyboardButton(text="👤 Foydalanuchi paneli")]
        
    ], resize_keyboard=True)

telefon_raqam=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Raqamni yuborish",request_contact=True)]
        
    ], resize_keyboard=True)


state_tugma = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kurs haqida malumot tugadi")]
        
    ], resize_keyboard=True)