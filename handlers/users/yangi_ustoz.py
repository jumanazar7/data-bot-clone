
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
from data.config import ADMINS
from loader import dp, db
from keyboards.default.dafaulttugma import admin_tugma
from states.main import ustoz
from keyboards.inline.inlinetugmalr import ha_yoq
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="📥 Yangi Ustoz", state="*", user_id=ADMINS)
async def send_reklama_title(message: types.CallbackQuery, state: FSMContext):
   await message.answer("Iltimos yangi ustoz ism familasi?")
   await state.finish()
   await ustoz.title.set()

@dp.message_handler(state=ustoz.title)
async def send_reklama(message: types.Message, state: FSMContext):
    await message.answer("Iltimos belgi yoki probilni orniga _ shuni qayub fan nomini qaytadan kirtsang giz !!")
    title = message.text
    await state.update_data(
        {"title": title}
    )
    await ustoz.next()

@dp.message_handler(state=ustoz.slog)
async def send_reklama(message: types.Message, state: FSMContext):
    await message.answer("Iltimos yangi ustozni ma'lumot nomasini yuboring !")
    slog = message.text
    await state.update_data(
        {"slog": slog}
    )
    await ustoz.next()

@dp.message_handler(state=ustoz.tajribasi)
async def send_reklama(message: types.Message, state: FSMContext):
    await message.answer("Rasm yubaring Faqat URL !")
    tajribasi = message.text
    await state.update_data(
        {"tajribasi": tajribasi}
    )
    await ustoz.next()


@dp.message_handler(state=ustoz.image_url)
async def send_reklama(message: types.Message, state: FSMContext):
    get_curses_info = db.select_all_curses()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in get_curses_info:
        markup.insert(InlineKeyboardButton(text=i[1],callback_data=i[2]))
    await message.answer("Qaysi Fan ustozi",reply_markup=markup)
    image_url = message.text
    await state.update_data(
        {"image_url": image_url}
    )
    await ustoz.next()

@dp.callback_query_handler(state=ustoz.sub_curses_id)
async def send_reklama(call: types.CallbackQuery, state: FSMContext):
    sub_curses_id = call.data  
    sub= db.select_all_curses_id(slog=sub_curses_id)
    await state.update_data(
        {"sub_curses_id": sub[0]}
    )
    data = await state.get_data()
    title = data.get("title")
    tajribasi = data.get("tajribasi")
    image_url = data.get("image_url")
    s2 = f"""Ism: {title}
Ma'lumot:{tajribasi}
Bazga ko'shilsinmi!"""
    try:
        await call.message.answer_photo(photo=image_url,caption=s2,reply_markup=ha_yoq)
        await ustoz.next()
    except:
        await call.message.reply("URL da Xatolik!",reply_markup=admin_tugma)

@dp.callback_query_handler(text = "ha",state=ustoz.tugatish)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    title = data.get("title")
    slog = data.get("slog")
    tajribasi = data.get("tajribasi")
    image_url = data.get("image_url")
    sub_curses_id = data.get("sub_curses_id")
    try:
        db.add_ustozlar(title=title,slog=slog,tajribasi=tajribasi,imge_url=image_url,sub_id=sub_curses_id)
        await call.message.answer("Bazaga ko'shildi!")
        await call.message.reply("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.answer("Ko'shilmadi xatolik!")  
      
   

      
       

    
 


