from loader import db,dp
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.inlinetugmalr import back,home
from states.main import Cursstate,murojat
from aiogram.dispatcher import FSMContext



@dp.callback_query_handler(text="back",state=murojat.oy)
async def back_to_home(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    slug = data.get("slug")

    m_curses = db.select_all_curses_ustozlar(slog=slug)
    cad_id = m_curses[0]
    await state.update_data({
        "slug" : slug
    })
    cad_maney = m_curses[3]
    cad_title = m_curses[1]
    cad_malumot = m_curses[4]
    cad_img = m_curses[5]
    ustozlar = db.select_all_ustozlar(sub_curses_id=cad_id)
    markup = InlineKeyboardMarkup(row_width=2)
    oylikreja = InlineKeyboardButton(text="Kurs dars rejasi", callback_data="oy")
    for i1 in ustozlar:
        markup.insert(InlineKeyboardButton(text=i1[1],callback_data=i1[2]))
    markup.add(back,home)
    markup.insert(oylikreja)
    if cad_img is not None:
        await call.message.delete()
        await call.message.answer_photo(photo=cad_img , caption=f"{cad_title}Boyich malumot\n\nNarh:{cad_maney}\n\nMa'lumot nomasi:\n{cad_malumot}",reply_markup=markup)
    else:
        await call.message.answer(f"{cad_title}Boyich malumot\n\nNarh:{cad_maney}\n\nMa'lumot nomasi:\n{cad_malumot}",reply_markup=markup)
    await Cursstate.ustozlar.set()



@dp.callback_query_handler(text="oy",state=Cursstate.ustozlar)
async def get_ustozlar(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    s1 = data.get("ID_OY")
    a = db.select_all_math(sub_curses_id=s1)
    markup = InlineKeyboardMarkup(row_width=6)
    for i1 in a:
            markup.insert(InlineKeyboardButton(text=i1[1],callback_data=i1[0]))
    markup.add(back,home)
    await call.message.delete()
    await call.message.answer("Oy ni tanlang",reply_markup=markup)
    await murojat.oy.set()



@dp.callback_query_handler(state=murojat.oy)
async def get_ustozlar(call: types.CallbackQuery, state: FSMContext):
    cad_slog = call.data
    data = await state.get_data()
    s1 = data.get("ID_OY")
    a = db.select_all_math(sub_curses_id=s1)
    markup = InlineKeyboardMarkup(row_width=6)
    for i1 in a:
            markup.insert(InlineKeyboardButton(text=i1[1],callback_data=i1[0]))
    markup.add(back,home)
    
    il = db.select_all_math(id=cad_slog)
    s = il[0][2]
    await call.message.delete()
    await call.message.answer(text=f"{s}",reply_markup=markup)
    await murojat.oy.set()
    
@dp.callback_query_handler(state=Cursstate.ustozlar)
async def get_ustozlar(call: types.CallbackQuery, state: FSMContext):
    cad_slog = call.data  
    u_db1 = db.select_all_ustozlar(slog=cad_slog)
    for u_db in u_db1:
        cad_title = u_db[1]
        cad_malumot = u_db[3]
        cad_img = u_db[4]
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(back,home)
    try:
        await call.message.delete()
        await call.message.answer_photo(photo=cad_img, caption=f"{cad_title} haqida m'lumot:\n\n{cad_malumot}", reply_markup=markup)
    except:
        await call.message.answer(f"{cad_title} haqida m'lumot:\n\n{cad_malumot}", reply_markup=markup)
    await Cursstate.next()