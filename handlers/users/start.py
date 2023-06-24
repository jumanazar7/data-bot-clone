import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inlinetugmalr import main_menu
from data.config import ADMINS
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from data.config import ADMINS

@dp.message_handler(text="👤 Foydalanuchi paneli", state="*",user_id=ADMINS)
async def bot_start(message: types.Message, state=FSMContext):
    await state.finish()
    name = message.from_user.full_name
    try:
        db.add_user(tg_id=message.from_user.id,full_name=name,username=message.from_user.username)
        await message.answer(f"Xush kelibsiz! {name} Bizsizni botimiz da korish dan xursand miz",reply_markup=main_menu)

        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"Xush kelibsiz! {name} Biz sizni botimizda ko'rishdan xursand miz ", reply_markup=main_menu)




@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state=FSMContext):
    await state.finish()
    name = message.from_user.full_name
    try:
        db.add_user(tg_id=message.from_user.id,full_name=name,username=message.from_user.username)
        await message.answer(f"Xush kelibsiz! {name} Bizsizni botimiz da korish dan xursand miz",reply_markup=main_menu)
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"Xush kelibsiz! {name} Biz sizni botimizda ko'rishdan xursand miz ", reply_markup=main_menu)

@dp.callback_query_handler(text="admin")
async def admin(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=b2e9498f012448856e74b7f7048fa21d-5876939-images-thumbs&n=13", caption="Admin: @SH_O_H_05")
