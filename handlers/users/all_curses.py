from loader import db,dp
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.inlinetugmalr import back,home
from states.main import Cursstate
from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text="max")
async def get_curses(call: types.CallbackQuery):
    get_curses_info = db.select_all_curses()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in get_curses_info:
        markup.insert(InlineKeyboardButton(text=i[1],callback_data=i[2]))
    markup.add(back)
    await call.message.edit_text("Barcha Yonalishlar\n\nBuyerdan siz istalgan fani tanlang va ma'lumot oling",reply_markup=markup)
    await Cursstate.curses.set()

@dp.callback_query_handler(state=Cursstate.curses)
async def get_curses_states(call: types.CallbackQuery, state: FSMContext):
    slug = call.data
    s1 = db.select_all_curses_id(slog=slug)
    await state.update_data({
        "ID_OY" : s1[0]
    })

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
        await call.message.answer_photo(photo=cad_img , caption=f"{cad_title}Boyich ma'lumot\n\nNarh:{cad_maney}\n\nMa'lumot nomasi:\n{cad_malumot}",reply_markup=markup)
    else:
        await call.message.answer(f"{cad_title}Boyich ma'lumot\n\nNarh:{cad_maney}\n\nMa'lumot nomasi:\n{cad_malumot}",reply_markup=markup)
    await Cursstate.next()


