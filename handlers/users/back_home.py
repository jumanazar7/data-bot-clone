from loader import dp, db
from aiogram import types
from states.main import Cursstate,Cursstate1
from aiogram.dispatcher import FSMContext
from keyboards.inline.inlinetugmalr import main_menu,back,home,ha_yoq
from  aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@dp.callback_query_handler(text="home",state="*")
async def back_to_home(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    firist_name= call["from"]["first_name"]
    name = call["from"]["last_name"]
    await call.message.answer(f"Xush kelibsiz! {firist_name} {name} Bizsizni botimiz da korish dan xursand miz",reply_markup=main_menu)



@dp.callback_query_handler(text="back",state=Cursstate1.curses)
async def back_to_home(call: types.CallbackQuery, state: FSMContext):
    firist_name= call["from"]["first_name"]
    name = call["from"]["last_name"]
    await call.message.edit_text(f"Xush kelibsiz! {firist_name} {name} Bizsizni botimiz da korish dan xursand miz",reply_markup=main_menu)
    await state.finish()    


@dp.callback_query_handler(text="back",state=Cursstate.curses)
async def back_to_home(call: types.CallbackQuery, state: FSMContext):
    firist_name= call["from"]["first_name"]
    name = call["from"]["last_name"]
    await call.message.edit_text(f"Xush kelibsiz! {firist_name} {name} Bizsizni botimiz da korish dan xursand miz",reply_markup=main_menu)
    await state.finish()    

@dp.callback_query_handler(text="back",state=Cursstate.ustozlar)
async def back_to_ustozlar(call: types.CallbackQuery, state: FSMContext):
    get_curses_info = db.select_all_curses()

    await call.message.delete()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in get_curses_info:
        markup.insert(InlineKeyboardButton(text=i[1],callback_data=i[2]))
    markup.add(back)
   
    await call.message.answer("Barcha fanlar o'zinggizga yokanini tanlang",reply_markup=markup)
    await Cursstate.curses.set()



@dp.callback_query_handler(text= "back",state=Cursstate.reja)
async def back_to_ustozlar(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()    
    cad_slog = data.get("slug")
    m_curses = db.select_all_curses_ustozlar(slog=cad_slog)
    cad_id = m_curses[0]
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
        await call.message.answer_photo(photo=cad_img , caption=f"{cad_title}Boyicha ma'lumot\n\nNarh:{cad_maney}\n\nMa'lumot nomasi:\n{cad_malumot}",reply_markup=markup)
    else:
        await call.message.answer(f"{cad_title} Boyicha ma'lumot\n\nNarh:{cad_maney}\n\nMa'lumot nomasi:\n{cad_malumot}",reply_markup=markup)
    await Cursstate.ustozlar.set()





