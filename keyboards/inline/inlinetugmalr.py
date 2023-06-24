from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import db
main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📙 Barcha fanlar",callback_data="max"),InlineKeyboardButton(text="🎞 Video darslar",callback_data="video_d")],
        [InlineKeyboardButton(text="📞 Admin bilan bog'lanish",callback_data="admin"),InlineKeyboardButton(text="🖋 Kursga yozilish",callback_data="kurs")]
    ]
)
back = InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")
home = InlineKeyboardButton(text="🏚 Bosh sahifa", callback_data="home")

main_menu_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📸 Suratli",callback_data="Surotbor"),InlineKeyboardButton(text="📝 Text",callback_data="notimge")],
        [InlineKeyboardButton(text="📹 Vidio",callback_data="vidio"),InlineKeyboardButton(text="Voice",callback_data="Voice")]
    ]
)

ha_yoq=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ha",callback_data="ha"),InlineKeyboardButton(text="Yoq",callback_data="yoq")],
    ]
)

HA_YOQ=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ha",callback_data="HA"),InlineKeyboardButton(text="Yoq",callback_data="yoq")],
    ]
)



numbers = InlineKeyboardMarkup(row_width=3)
for i in range(1,13):
    numbers.insert(InlineKeyboardButton(text=i,callback_data=f"{i}"))

