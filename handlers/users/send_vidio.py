import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
from keyboards.default.dafaulttugma import admin_tugma,state_tugma
from states.main import Cursstate,back_to_video,insert_to_video,Cursstate1
from keyboards.inline.inlinetugmalr import main_menu_admin,main_menu,back,home
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import sqlite3

@dp.callback_query_handler(text="video_d",user_id=ADMINS)
async def get_curses(call: types.CallbackQuery):
    get_curses_info = db.select_all_curses()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in get_curses_info:
        markup.insert(InlineKeyboardButton(text=i[1],callback_data=i[2]))
    markup.add(back)
    await call.message.edit_text("Fani tanlang va bepul video darslik koring !",reply_markup=markup)
    await Cursstate1.curses.set()

@dp.callback_query_handler(state=Cursstate1.curses)
async def dars_videio(call : types.CallbackQuery, state: FSMContext):
    cad_slog = call.data
    await state.update_data({
        "cad_slog_fan": cad_slog
    })
    s = db.select_all_curses_id(slog=cad_slog)
    s1 = db.select_video(sub_curses_id=s[0])
    markup = InlineKeyboardMarkup(row_width=2)
    for i in s1:
        markup.insert(InlineKeyboardButton(text=i[-1],callback_data=i[1]))
    markup.add(back,home)
    await call.message.edit_text("Dars ni tanlang !",reply_markup=markup)
    await back_to_video.video.set()

@dp.callback_query_handler(text="back",state=back_to_video.video)
async def get_curses_back(call: types.CallbackQuery):
    get_curses_info = db.select_all_curses()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in get_curses_info:
        markup.insert(InlineKeyboardButton(text=i[1],callback_data=i[2]))
    markup.add(back)
    await call.message.edit_text("Fani tanlang va bepul video darslik koring !",reply_markup=markup)
    await Cursstate.curses.set()


@dp.callback_query_handler(state=back_to_video.video)
async def get_curses_back(call: types.CallbackQuery,state: FSMContext):
    cad_slug = call.data
    s = db.select_video(slog=cad_slug)
    text = s[0][2]
    file_id = s[0][3]
    await call.message.answer_video(video=file_id,caption=text)



@dp.message_handler(content_types=["video"],user_id=ADMINS)
async def send_vidyi(message: types.Message, state:FSMContext):
    file_id = message['video']['file_id']
    print(file_id)
    await state.update_data({
        "file_id": file_id
    })
    get_curses_info = db.select_all_curses()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in get_curses_info:
        markup.insert(InlineKeyboardButton(text=i[1],callback_data=i[2]))
    await message.answer("Qaysi fan video draslikgi",reply_markup=markup)
    await insert_to_video.fan.set()

@dp.callback_query_handler(state=insert_to_video.fan)
async def get_fan(call: types.CallbackQuery, state: FSMContext):
    cad_slog = call.data
    s =db.select_all_curses_id(slog=cad_slog)
    await state.update_data({
        "sub_id_video":s[0]
    })
    await call.message.answer("Fanni nomi va nechanchi dars ekanligini kiriritng\nMasalan: Mobilografiya_1_dars")
    await insert_to_video.sub_id.set()

@dp.message_handler(state=insert_to_video.sub_id)
async def insert_slug(message: types.Message, state : FSMContext):
    slug = message["text"]
    await state.update_data({
        "video_slug":slug
    })
    await message.answer("Video Haqida tushuncha bering")
    await insert_to_video.malumot.set()

@dp.message_handler(state=insert_to_video.malumot)
async def insert_malumot(message: types.Message, state : FSMContext):
    malumot = message["text"]
    await state.update_data({
        "video_malumot":malumot
    })
    await message.answer("Nechanchi video dars\nMasalan:1-dars")
    await insert_to_video.reja.set()

@dp.message_handler(state=insert_to_video.reja)
async def insert_video(message: types.Message, state : FSMContext):
    name = message["text"]
    data = await state.get_data()
    file_od_id = data.get("file_id")
    sub_id = data.get("sub_id_video")
    coapshin = data.get("video_malumot")
    slug = data.get("video_slug")
    try:
        db.add_video(slog=slug,tajribasi=coapshin,file_id=file_od_id,sub_id=sub_id,name=name)
        await message.answer("Video koshildi",reply_markup=admin_tugma)
        await state.finish()
    except:
        await state.finish()
        await message.answer("Xatolik !!",reply_markup=admin_tugma)
