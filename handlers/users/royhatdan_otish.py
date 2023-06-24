import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.inlinetugmalr import HA_YOQ
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
from keyboards.default.dafaulttugma import telefon_raqam
from keyboards.inline.inlinetugmalr import main_menu
from states.main import royhat_sate
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

   

@dp.callback_query_handler(text="HA",state=royhat_sate.ha)
async def ha(call : types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    data = await state.get_data()
    fan = data.get("fan")
    number = data.get("number")
    ism = call["from"]["first_name"]
    familya = call["from"]["last_name"]
    username = call["from"]["username"]
    s2 = f"""Fan nomi: {fan}
Ism: {ism}
Familya: {familya}
Username: @{username}
Telefon Raqam: +{number}"""
    await bot.send_message(chat_id=ADMINS[1],text=s2)
    await call.message.answer("Adminga yuborildi!")
    firist_name= call["from"]["first_name"]
    name = call["from"]["last_name"]
    await call.message.answer(f"Xush kelibsiz! {firist_name} {name} Bizsizni botimiz da korish dan xursand miz",reply_markup=main_menu)



   
@dp.callback_query_handler(text="kurs")
async def royhat(call: types.CallbackQuery,state: FSMContext):
    get_curses_info = db.select_all_curses()
    await call.message.delete()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in get_curses_info:
        markup.insert(InlineKeyboardButton(text=i[1],callback_data=i[2]))
    await call.message.answer("Fani tanlang !",reply_markup=markup)
    await royhat_sate.ism.set()

@dp.callback_query_handler(state=royhat_sate.ism)
async def get_curs(call: types.CallbackQuery,state:FSMContext):
    cat_slug = call["data"]
    await call.message.answer("Raqanmi yuborin",reply_markup=telefon_raqam)
    s =  db.select_all_curses_ustozlar(slog=cat_slug)
    await call.message.delete()
    await state.update_data({
        "fan" : s[1]
    })
    await royhat_sate.next()


@dp.message_handler(content_types=["contact"],state=royhat_sate.curs)
async def get_curs(message: types.Message,state:FSMContext):
    await message.answer("Malumotlaring giz",reply_markup=ReplyKeyboardRemove())
    number = message["contact"]["phone_number"]
    data = await state.get_data()
    fan = data.get("fan")
    ism = message["from"]["first_name"]
    familya = message["from"]["last_name"]
    username = message["from"]["username"]
    await state.update_data({
        "number" : number
    })
    s2 = f"""Fan nomi: {fan}
Ism: {ism}
Familya: {familya}
Username: @{username}
Telefon Raqam: +{number}
"""
    await message.answer(s2,reply_markup=HA_YOQ)
    await royhat_sate.next()

