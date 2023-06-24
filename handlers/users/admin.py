import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.inlinetugmalr import home
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
from keyboards.default.dafaulttugma import admin_tugma,state_tugma
from states.main import reklama,Yangi_kurs_1,delete_state,delete_ustoz
from keyboards.inline.inlinetugmalr import main_menu_admin,main_menu
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import sqlite3

def deleteRecord(id):
        try:
            sqliteConnection = sqlite3.connect('main1.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sql = """DELETE FROM COURSE WHERE id=?;"""
            cursor.execute(sql, (id, ))
            sqliteConnection.commit()
            print("deleted ")
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")


@dp.message_handler(text="👤 Foydalanuchi paneli", state="*",user_id=ADMINS)
async def bot_start(message: types.Message, state=FSMContext):
    await state.finish()
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(tg_id=message.from_user.id,full_name=name,username=message.from_user.username)
        await message.answer(f"Xush kelibsiz! {name} Bizsizni botimiz da korish dan hursatnt miz",reply_markup=main_menu)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"Xush kelibsiz! {name} Biz sizni botimizda ko'rishdan hursant miz ", reply_markup=main_menu)





@dp.message_handler(text="👤 Barcha Foydalanuchilar", state="*", user_id=ADMINS)
async def get_all_users(message: types.Message,state=FSMContext):
    await state.finish()
    users = db.select_all_users()
    id = []
    name = []
    for user in users:
        id.append(user[0])
        name.append(user[1])
    data = {
        "Telegram ID": id,
        "Name": name
    }
    pd.options.display.max_rows = 10000
    df = pd.DataFrame(data)
    if len(df) > 50:
        for x in range(0, len(df), 50):
            await bot.send_message(message.chat.id, df[x:x + 50])
    else:
       await bot.send_message(message.chat.id, df)
       

@dp.message_handler(text="🗣 Reklama yubor", state="*",user_id=ADMINS)
async def send_ad_to_all(message: types.Message, state=FSMContext):
    await message.answer("Reklama haqida ma'lumot bering",reply_markup=main_menu_admin)
    await reklama.birinchi.set()

@dp.message_handler(text="/start",state="*", user_id=ADMINS)
async def start_admin(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Admin paneliga xush kelibsz",reply_markup=admin_tugma)
    
@dp.message_handler(text="❌ Fani o'chirish",state="*",user_id=ADMINS)
async def delete_curses6(message: types.Message,state:FSMContext):
    get_curses_info = db.select_all_curses()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in get_curses_info:
        markup.insert(InlineKeyboardButton(text=i[1],callback_data=i[2]))
    markup.add(home)
    await message.answer_photo(photo="https://www.pxpng.com/public/uploads/preview/-11602611763nkkt4x1pa1.png",caption="Qaysi fanni o'chirmoqchisz",reply_markup=markup)
    await delete_state.ochir.set()

@dp.callback_query_handler(state=delete_state.ochir)
async def delete_curses_id(call:types.CallbackQuery, state:FSMContext):
    cad_slog = call.data  
    s = db.select_all_curses_id(slog=cad_slog)
    try:
        db.delete_curses(s[0])
        db.delete_curses_math(s[0])
        db.delete_ustozlar_sub(s[0])
        await call.message.delete()
        await call.message.answer("Vazifa bajarildi",reply_markup=admin_tugma)
        await state.finish()
    except:
        await call.message.delete()
        await call.message.answer("Vazifa bajarilmadi!",reply_markup=admin_tugma)
        await state.finish()

@dp.message_handler(text="❌ Ustozni O'chirish",state="*",user_id=ADMINS)
async def delete_curses(message: types.Message,state:FSMContext):
    get_curses_info = db.select_all_Ustozlar()
    markup = InlineKeyboardMarkup(row_width=2)
    for i in get_curses_info:
        markup.insert(InlineKeyboardButton(text=i[1],callback_data=i[0]))
    markup.add(home)
    await message.answer_photo(photo="https://www.pxpng.com/public/uploads/preview/-11602611763nkkt4x1pa1.png",caption="Qaysi fanni o'chirmoqchisiz. Sh fanga tegishli bar ma'lumotlar ochishi mumkin shu jumladan ustozlar ham",reply_markup=markup)
    await delete_ustoz.ochir.set()

@dp.callback_query_handler(state=delete_ustoz.ochir)
async def delete_curses_id(call:types.CallbackQuery, state:FSMContext):
    cad_slog = call.data  
    s = db.select_all_Ustozlar_id(id=cad_slog)

    try:
        db.delete_ustozlar(s[0])
        await call.message.delete()
        await call.message.answer("Vazifa bajarildi",reply_markup=admin_tugma)
        await state.finish()
    except:
        await call.message.delete()
        await call.message.answer("Vazifa bajarilmadi!",reply_markup=admin_tugma)
        await state.finish()

@dp.message_handler(text="📥 Yangi Fan", state="*", user_id=ADMINS)
async def send_reklama_title(message: types.CallbackQuery, state: FSMContext):
   await message.answer("Iltimos fan nomi?")
   await state.finish()
   await Yangi_kurs_1.title.set()

@dp.message_handler(state=Yangi_kurs_1.title)
async def send_reklama6(message: types.Message, state: FSMContext):
    await message.answer("Iltimos belgi yoki probilni orniga _ shuni qayub fan nomini qaytadan kirtsang giz !!")
    title = message.text
    await state.update_data(
        {"title": title}
    )
    await Yangi_kurs_1.next()


@dp.message_handler(state=Yangi_kurs_1.slug)
async def send_reklama5(message: types.Message, state: FSMContext):
    await message.answer("Iltimos kurs narhini kiriting!")
    slug = message.text
    await state.update_data(
        {"slug": slug}
    )
    await Yangi_kurs_1.next()



@dp.message_handler(state=Yangi_kurs_1.maney)
async def send_reklama4(message: types.Message, state: FSMContext):
    await message.answer("Iltimos kurs haqida kisqa ma'lumot bering")
    maney = message.text
    await state.update_data(
        {"puli": maney}
    )
    await Yangi_kurs_1.next()


@dp.message_handler(state=Yangi_kurs_1.malumot)
async def send_reklama3(message: types.Message, state: FSMContext):
    await message.answer("Iltimos rasm yuboring faqat URL agrada fan panelda chiqmasa demak URL da hatolik bor")
    malumot = message.text
    await state.update_data(
        {"malumot": malumot}
    )
    await Yangi_kurs_1.next()


@dp.message_handler(state=Yangi_kurs_1.imge_url)
async def send_reklama2(message: types.Message, state: FSMContext):
    await message.answer("1-oyda nima rejalar bor")
    imge_url = message.text
    await state.update_data(
        {"imge_url": imge_url}
    )
    await Yangi_kurs_1.next()    


@dp.message_handler(state=Yangi_kurs_1.birinchioy)
async def send_reklama1(message: types.Message, state: FSMContext):
    await message.answer("2-oyda nima rejalar bor",reply_markup=state_tugma)
    birinchioy = message.text
    await state.update_data(
        {"birinchioy": birinchioy}
    )
    await Yangi_kurs_1.next()


@dp.message_handler(state=Yangi_kurs_1.ikkichioy)
async def send_reklama6(message: types.Message, state: FSMContext):
    await message.answer("3-oyda nima rejalar bor",reply_markup=state_tugma)
    ikkichioy = message.text
    await state.update_data(
        {"ikkichioy": ikkichioy}
    )
    await Yangi_kurs_1.next()


@dp.message_handler(state=Yangi_kurs_1.uchchioy)
async def send_reklama7(message: types.Message, state: FSMContext):
    await message.answer("4-oyda nima rejalar bor",reply_markup=state_tugma)
    uchchioy = message.text
    await state.update_data(
        {"uchchioy": uchchioy}
    )
    await Yangi_kurs_1.next()


@dp.message_handler(state=Yangi_kurs_1.tortchioy)
async def send_reklama88(message: types.Message, state: FSMContext):
    await message.answer("5-oyda nima rejalar bor",reply_markup=state_tugma)
    tortchioy = message.text
    await state.update_data(
        {"tortchioy": tortchioy}
    )
    await Yangi_kurs_1.next()

@dp.message_handler(state=Yangi_kurs_1.beshchioy)
async def send_reklama8(message: types.Message, state: FSMContext):
    await message.answer("6-oyda nima rejalar bor",reply_markup=state_tugma)
    beshchioy = message.text
    await state.update_data(
        {"beshchioy": beshchioy}
    )
    await Yangi_kurs_1.next()


@dp.message_handler(state=Yangi_kurs_1.oltichioy)
async def send_reklama9(message: types.Message, state: FSMContext):
    await message.answer("7-oyda nima rejalar bor",reply_markup=state_tugma)
    oltichioy = message.text
    await state.update_data(
        {"oltichioy": oltichioy}
    )
    await Yangi_kurs_1.next()

@dp.message_handler(state=Yangi_kurs_1.yettichioy)
async def send_reklama10(message: types.Message, state: FSMContext):
    await message.answer("8-oyda nima rejalar bor",reply_markup=state_tugma)
    yettichioy = message.text
    await state.update_data(
        {"yettichioy": yettichioy}
    )
    await Yangi_kurs_1.next()


@dp.message_handler(state=Yangi_kurs_1.sakizchioy)
async def send_reklama11(message: types.Message, state: FSMContext):
    await message.answer("9-oyda nima rejalar bor",reply_markup=state_tugma)
    sakizchioy = message.text
    await state.update_data(
        {"sakizchioy": sakizchioy}
    )
    await Yangi_kurs_1.next()
    
@dp.message_handler(state=Yangi_kurs_1.tqqizinchioy)
async def send_reklama12(message: types.Message, state: FSMContext):
    await message.answer("10-oyda nima rejalar bor",reply_markup=state_tugma)
    tqqizinchioy = message.text
    await state.update_data(
        {"tqqizinchioy": tqqizinchioy}
    )
    await Yangi_kurs_1.next()

@dp.message_handler(state=Yangi_kurs_1.onchioy)
async def send_reklama21(message: types.Message, state: FSMContext):
    await message.answer("11-oyda nima rejalar bor",reply_markup=state_tugma)
    onchioy = message.text
    await state.update_data(
        {"onchioy": onchioy}
    )
    await Yangi_kurs_1.next()

@dp.message_handler(state=Yangi_kurs_1.onbirchioy)
async def send_reklama15(message: types.Message, state: FSMContext):
    await message.answer("12-oyda nima rejalar bor",reply_markup=state_tugma)
    onbirchioy = message.text
    await state.update_data(
        {"onbirchioy": onbirchioy}
    )
    await Yangi_kurs_1.next()

@dp.message_handler(state=Yangi_kurs_1.onikkichioy)
async def send_reklama14(message: types.Message, state: FSMContext):
    await message.answer("Tugadish",reply_markup=state_tugma)
    onikki = message.text
    await state.update_data(
        {"onikkichioy": onikki}
    )
    await Yangi_kurs_1.tugadi.set()




@dp.callback_query_handler(text="Suratli",state=reklama.birinchi)
async def send_reklama_title(call: types.CallbackQuery, state: FSMContext):
   await call.message.answer("Iltimos reklamani tashlang")
   await reklama.suratli.set()



@dp.callback_query_handler(text="Video",state=reklama.birinchi)
async def send_reklama_titl7e(call: types.CallbackQuery, state: FSMContext):
   await call.message.answer("Iltimos reklamani tashlang")
   await reklama.vidio.set()


@dp.callback_query_handler(text="Voice",state=reklama.birinchi)
async def send_reklama_tit8le(call: types.CallbackQuery, state: FSMContext):
   await call.message.answer("Iltimos reklamani tashlang")
   await reklama.Voice.set()

@dp.callback_query_handler(text="Suratli",state=reklama.birinchi)
async def send_reklama_t7itle(call: types.CallbackQuery, state: FSMContext):
   await call.message.answer("Iltimos reklamani tashlang")
   await reklama.suratsz.set()



@dp.message_handler(content_types=["voice"],state=reklama.Voice)
async def send_reklama(message: types.Message, state: FSMContext):
    voice_id = message.voice.file_id
    users = db.select_all_users()
    yuborildi = 0
    yuborilmadi = 0
    count = db.count_users()[0]

    for user in users:
        user_id = user[1]
        try:
            yuborildi+=1
            await bot.send_voice(chat_id=user_id,voice=voice_id)
            await asyncio.sleep(0.05)
            await state.finish()
        except:
            yuborilmadi+=1
    await message.reply(f"Manashuncha {yuborildi} odamga yuborildi.\n\nManashuncha {yuborilmadi} odamga yuborilmadi.\n\nBazada {count} ta foydalanuvchi bor.")



@dp.message_handler(content_types=["photo"],state=reklama.suratli)
async def send_rekl9ama(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    caotion = message["caption"]
    users = db.select_all_users()
    yuborildi = 0
    yuborilmadi = 0
    count = db.count_users()[0]

    for user in users:
        user_id = user[1]
        try:
            yuborildi+=1
            await bot.send_photo(chat_id=user_id,photo=photo_id, caption=caotion)
            await asyncio.sleep(0.05)
            await state.finish()
        except:
            yuborilmadi+=1
    await message.reply(f"Manashuncha {yuborildi} odamga yuborildi.\n\nManashuncha {yuborilmadi} odamga yuborilmadi.\n\nBazada {count} ta foydalanuvchi bor.")
    



@dp.message_handler(state=reklama.suratsz)
async def send_rek7lama(call: types.Message, state: FSMContext):
    users = db.select_all_users()
    mesage = call["text"]
    yuborildi = 0
    yuborilmadi = 0
    count = db.count_users()[0]

    for user in users:
        user_id = user[1]
        try:
            yuborildi+=1
            await bot.send_message(chat_id=user_id, text=mesage)
            await asyncio.sleep(0.05)
            await state.finish()
        except:
            yuborilmadi+=1
    await call.reply(f"Manashuncha {yuborildi} odamga yuborildi.\n\nManashuncha {yuborilmadi} odamga yuborilmadi.\n\nBazada {count} ta foydalanuvchi bor.")


@dp.message_handler(state=reklama.vidio)
async def send_re6kl6ama(message: types.Message, state: FSMContext):
    await message.reply("Xatolik!",reply_markup=admin_tugma)


@dp.message_handler(state=reklama.Voice)
async def send_r14eklama(message: types.Message, state: FSMContext):
    await message.reply("Xatolik!",reply_markup=admin_tugma)


@dp.message_handler(state=reklama.suratsz)
async def send_r87ek6lama(message: types.Message, state: FSMContext):
    await message.reply("Xatolik!",reply_markup=admin_tugma)


@dp.message_handler(state=reklama.suratli)
async def send_re5klama(message: types.Message, state: FSMContext):
    await message.reply("Xatolik!",reply_markup=admin_tugma)

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")


