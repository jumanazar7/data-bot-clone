from loader import dp, db
from aiogram import types
from states.main import Yangi_kurs_1,Yangi_kurs
from aiogram.dispatcher import FSMContext
from keyboards.inline.inlinetugmalr import ha_yoq
from keyboards.default.dafaulttugma import admin_tugma
from data.config import ADMINS

@dp.callback_query_handler(text = "yoq",state="*",user_id=ADMINS)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
   await call.message.delete()
   await call.message.answer("Asosiy menu",reply_markup=admin_tugma)



@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.ikkichioy)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.ikkichioy.set()
    except:
        await message.reply("Suratning  URL da hatolik",reply_markup=admin_tugma)



@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.uchchioy)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.uchchioy.set()
    except:
        await message.reply("Suratning  URL da hatolik /start",reply_markup=admin_tugma)    


@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.tortchioy)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.tortchioy.set()
    except:
        await message.reply("Suratning  URL da hatolik /start",reply_markup=admin_tugma) 


@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.beshchioy)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")

    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.beshchioy.set()
    except:
        await message.reply("Suratning  URL da hatolik /start",reply_markup=admin_tugma) 


@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.oltichioy)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.oltichioy.set()
    except:
        await message.reply("Suratning  URL da hatolik /start",reply_markup=admin_tugma)         


@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.yettichioy)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.yettichioy.set()
    except:
        await message.reply("Suratning  URL da hatolik /start",reply_markup=admin_tugma) 


@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.sakizchioy)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.sakizchioy.set()
    except:
        await message.reply("Suratning  URL da hatolik /start",reply_markup=admin_tugma) 


@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.tqqizinchioy)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.tqqizinchioy.set()
    except:
        await message.reply("Suratning  URL da hatolik /start",reply_markup=admin_tugma) 


@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.onchioy)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.onchioy.set()
    except:
        await message.reply("Suratning  URL da hatolik /start",reply_markup=admin_tugma) 


@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.onbirchioy)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uchiinchioy = data.get("uchchioy")
    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.onikkichioy.set()
    except:
        await message.reply("Suratning  URL da hatolik /start",reply_markup=admin_tugma) 


@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.onikkichioy)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uchiinchioy = data.get("uchchioy")
    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.tugadi.set()
    except:
        await message.reply("Suratning  URL da hatolik /start",reply_markup=admin_tugma) 

@dp.message_handler(text="Kurs haqida malumot tugadi",state=Yangi_kurs_1.tugadi)
async def get_ism(message: types.Message, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    s = f"""Yang fan nomi: {title}.
Narh: {maney}.
Ma'lumot: {malumot}
""" 
    try:
        await message.answer_photo(photo=imge_url,caption=s,reply_markup=ha_yoq)    
        await Yangi_kurs.tugadi1.set()
    except:
        await message.reply("Suratning  URL da hatolik /start",reply_markup=admin_tugma) 

@dp.callback_query_handler(text ="ha",state=Yangi_kurs.ikkichioy)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!")    


@dp.callback_query_handler(text = "ha",state=Yangi_kurs.uchchioy)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)    


@dp.callback_query_handler(text = "ha",state=Yangi_kurs.tortchioy)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uch = data.get("uchchioy")

    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        db.add_curses_math(slog=3,oylik_reja=uch,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)    


@dp.callback_query_handler(text = "ha",state=Yangi_kurs.beshchioy)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uch = data.get("uchchioy")
    tort = data.get("tortchioy")
    try:                    
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        db.add_curses_math(slog=3,oylik_reja=uch,sub_id=count)
        db.add_curses_math(slog=4,oylik_reja=tort,sub_id=count)
      
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)  

@dp.callback_query_handler(text = "ha",state=Yangi_kurs.oltichioy)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uch = data.get("uchchioy")
    tort = data.get("tortchioy")
    besh= data.get("beshchioy")
    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        db.add_curses_math(slog=3,oylik_reja=uch,sub_id=count)
        db.add_curses_math(slog=4,oylik_reja=tort,sub_id=count)
        db.add_curses_math(slog=5,oylik_reja=besh,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)  



@dp.callback_query_handler(text = "ha",state=Yangi_kurs.yettichioy)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uch = data.get("uchchioy")
    tort = data.get("tortchioy")
    besh= data.get("beshchioy")
    olti = data.get("oltichioy")
    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        db.add_curses_math(slog=3,oylik_reja=uch,sub_id=count)
        db.add_curses_math(slog=4,oylik_reja=tort,sub_id=count)
        db.add_curses_math(slog=5,oylik_reja=besh,sub_id=count)
        db.add_curses_math(slog=6,oylik_reja=olti,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)  


@dp.callback_query_handler(text = "ha",state=Yangi_kurs.sakizchioy)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uch = data.get("uchchioy")
    tort = data.get("tortchioy")
    besh= data.get("beshchioy")
    olti = data.get("oltichioy")
    yetti = data.get("yettichioy")
    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        db.add_curses_math(slog=3,oylik_reja=uch,sub_id=count)
        db.add_curses_math(slog=4,oylik_reja=tort,sub_id=count)
        db.add_curses_math(slog=5,oylik_reja=besh,sub_id=count)
        db.add_curses_math(slog=6,oylik_reja=olti,sub_id=count)
        db.add_curses_math(slog=7,oylik_reja=yetti,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)  
 



@dp.callback_query_handler(text = "ha",state=Yangi_kurs.tqqizinchioy)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uch = data.get("uchchioy")
    tort = data.get("tortchioy")
    besh= data.get("beshchioy")
    olti = data.get("oltichioy")
    yetti = data.get("yettichioy")
    sakiz = data.get("sakizchioy")
    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        db.add_curses_math(slog=3,oylik_reja=uch,sub_id=count)
        db.add_curses_math(slog=4,oylik_reja=tort,sub_id=count)
        db.add_curses_math(slog=5,oylik_reja=besh,sub_id=count)
        db.add_curses_math(slog=6,oylik_reja=olti,sub_id=count)
        db.add_curses_math(slog=7,oylik_reja=yetti,sub_id=count)
        db.add_curses_math(slog=8,oylik_reja=sakiz,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)  


@dp.callback_query_handler(text = "ha",state=Yangi_kurs.onchioy)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uch = data.get("uchchioy")
    tort = data.get("tortchioy")
    besh= data.get("beshchioy")
    olti = data.get("oltichioy")
    yetti = data.get("yettichioy")
    sakiz = data.get("sakizchioy")
    toqiz = data.get("tqqizinchioy")
    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        db.add_curses_math(slog=3,oylik_reja=uch,sub_id=count)
        db.add_curses_math(slog=4,oylik_reja=tort,sub_id=count)
        db.add_curses_math(slog=5,oylik_reja=besh,sub_id=count)
        db.add_curses_math(slog=6,oylik_reja=olti,sub_id=count)
        db.add_curses_math(slog=7,oylik_reja=yetti,sub_id=count)
        db.add_curses_math(slog=8,oylik_reja=sakiz,sub_id=count)
        db.add_curses_math(slog=9,oylik_reja=toqiz,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)  


@dp.callback_query_handler(text = "ha",state=Yangi_kurs.onbirchioy)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uch = data.get("uchchioy")
    tort = data.get("tortchioy")
    besh= data.get("beshchioy")
    olti = data.get("oltichioy")
    yetti = data.get("yettichioy")
    sakiz = data.get("sakizchioy")
    toqiz = data.get("tqqizinchioy")
    on = data.get("onchioy")
    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        db.add_curses_math(slog=3,oylik_reja=uch,sub_id=count)
        db.add_curses_math(slog=4,oylik_reja=tort,sub_id=count)
        db.add_curses_math(slog=5,oylik_reja=besh,sub_id=count)
        db.add_curses_math(slog=6,oylik_reja=olti,sub_id=count)
        db.add_curses_math(slog=7,oylik_reja=yetti,sub_id=count)
        db.add_curses_math(slog=8,oylik_reja=sakiz,sub_id=count)
        db.add_curses_math(slog=9,oylik_reja=toqiz,sub_id=count)
        db.add_curses_math(slog=10,oylik_reja=on,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)  

 
@dp.callback_query_handler(text = "ha",state=Yangi_kurs.onikkichioy)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uch = data.get("uchchioy")
    tort = data.get("tortchioy")
    besh= data.get("beshchioy")
    olti = data.get("oltichioy")
    yetti = data.get("yettichioy")
    sakiz = data.get("sakizchioy")
    toqiz = data.get("tqqizinchioy")
    on = data.get("onchioy")
    onbir = data.get("onbirchioy")
    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        db.add_curses_math(slog=3,oylik_reja=uch,sub_id=count)
        db.add_curses_math(slog=4,oylik_reja=tort,sub_id=count)
        db.add_curses_math(slog=5,oylik_reja=besh,sub_id=count)
        db.add_curses_math(slog=6,oylik_reja=olti,sub_id=count)
        db.add_curses_math(slog=7,oylik_reja=yetti,sub_id=count)
        db.add_curses_math(slog=8,oylik_reja=sakiz,sub_id=count)
        db.add_curses_math(slog=9,oylik_reja=toqiz,sub_id=count)
        db.add_curses_math(slog=10,oylik_reja=on,sub_id=count)
        db.add_curses_math(slog=11,oylik_reja=onbir,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)  



@dp.callback_query_handler(text = "ha",state=Yangi_kurs.tugadi)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uch = data.get("uchchioy")
    tort = data.get("tortchioy")
    besh= data.get("beshchioy")
    olti = data.get("oltichioy")
    yetti = data.get("yettichioy")
    sakiz = data.get("sakizchioy")
    toqiz = data.get("tqqizinchioy")
    on = data.get("onchioy")
    onbir = data.get("onbirchioy")
    onikki = data.get("onikkichioy")
    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        db.add_curses_math(slog=3,oylik_reja=uch,sub_id=count)
        db.add_curses_math(slog=4,oylik_reja=tort,sub_id=count)
        db.add_curses_math(slog=5,oylik_reja=besh,sub_id=count)
        db.add_curses_math(slog=6,oylik_reja=olti,sub_id=count)
        db.add_curses_math(slog=7,oylik_reja=yetti,sub_id=count)
        db.add_curses_math(slog=8,oylik_reja=sakiz,sub_id=count)
        db.add_curses_math(slog=9,oylik_reja=toqiz,sub_id=count)
        db.add_curses_math(slog=10,oylik_reja=on,sub_id=count)
        db.add_curses_math(slog=11,oylik_reja=onbir,sub_id=count)
        db.add_curses_math(slog=12,oylik_reja=onikki,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)  


@dp.callback_query_handler(text = "ha",state=Yangi_kurs.tugadi1)
async def get_bir(call: types.CallbackQuery, state: FSMContext):
    data= await state.get_data()
    title = data.get("title")
    slug = data.get("slug")
    maney = data.get("puli")
    malumot = data.get("malumot")
    imge_url = data.get("imge_url")
    birinchioy = data.get("birinchioy")
    ikkichioy = data.get("ikkichioy")
    uch = data.get("uchchioy")
    tort = data.get("tortchioy")
    besh= data.get("beshchioy")
    olti = data.get("oltichioy")
    yetti = data.get("yettichioy")
    sakiz = data.get("sakizchioy")
    toqiz = data.get("tqqizinchioy")
    on = data.get("onchioy")
    onbir = data.get("onbirchioy")
    onikki = data.get("onikkichioy")
    try:
        db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
        count = db.count_curses()[0]
        db.add_curses_math(slog=1,oylik_reja=birinchioy,sub_id=count)
        db.add_curses_math(slog=2,oylik_reja=ikkichioy,sub_id=count)
        db.add_curses_math(slog=3,oylik_reja=uch,sub_id=count)
        db.add_curses_math(slog=4,oylik_reja=tort,sub_id=count)
        db.add_curses_math(slog=5,oylik_reja=besh,sub_id=count)
        db.add_curses_math(slog=6,oylik_reja=olti,sub_id=count)
        db.add_curses_math(slog=7,oylik_reja=yetti,sub_id=count)
        db.add_curses_math(slog=8,oylik_reja=sakiz,sub_id=count)
        db.add_curses_math(slog=9,oylik_reja=toqiz,sub_id=count)
        db.add_curses_math(slog=10,oylik_reja=on,sub_id=count)
        db.add_curses_math(slog=11,oylik_reja=onbir,sub_id=count)
        db.add_curses_math(slog=12,oylik_reja=onikki,sub_id=count)
        await call.message.delete()
        await call.message.answer("Kurs bazaga ko'shildi!")
        await call.message.answer("Tabriklayman!",reply_markup=admin_tugma)
    except:
        await call.message.delete()
        await call.message.answer("Kurs ko'shilmadi hatolik!",reply_markup=admin_tugma)  

    











# @dp.message_handler(state=Yangi_kurs.tortchioy)
# async def get_bir(message: types.Message, state: FSMContext):
#     data= await state.get_data()
#     title = data.get("title")
#     slug = data.get("slug")
#     maney = data.get("puli")
#     malumot = data.get("malumot")
#     imge_url = data.get("imge_url")
#     birinchioy = data.get("birinchioy")
#     ikkichioy = data.get("ikkichioy")
#     uch = data.get("uchchioy")
#     s2 = (birinchioy,ikkichioy,uch)
#     s=1
#     try:
#         db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
#         count = db.count_curses()[0]
#         for i in s2:
#             s+=1
#             db.add_curses_math(slog=s,oylik_reja=i,sub_id=count)
#         await message.answer("Kurs bazaga ko'shildi!")
#         await Yangi_kurs.next()
#     except:
#         await message.answer("Kurs ko'shilmadi hatolik!")    
    

# @dp.message_handler(state=Yangi_kurs.beshchioy)
# async def get_bir(message: types.Message, state: FSMContext):
#     data= await state.get_data()
#     title = data.get("title")
#     slug = data.get("slug")
#     maney = data.get("puli")
#     malumot = data.get("malumot")
#     imge_url = data.get("imge_url")
#     birinchioy = data.get("birinchioy")
#     ikkichioy = data.get("ikkichioy")
#     uch = data.get("uchchioy")
#     tort = data.get("tortchioy")
#     s2 = (birinchioy,ikkichioy,uch,tort)
#     s=1
#     try:
#         db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
#         count = db.count_curses()[0]
#         for i in s2:
#             s+=1
#             db.add_curses_math(slog=5,oylik_reja=i,sub_id=count)
#         await message.answer("Kurs bazaga ko'shildi!")
#     except:
#         await message.answer("Kurs ko'shilmadi hatolik!")


# @dp.message_handler(state=Yangi_kurs.oltichioy)
# async def get_bir(message: types.Message, state: FSMContext):
#     data= await state.get_data()
#     title = data.get("title")
#     slug = data.get("slug")
#     maney = data.get("puli")
#     malumot = data.get("malumot")
#     imge_url = data.get("imge_url")
#     birinchioy = data.get("birinchioy")
#     ikkichioy = data.get("ikkichioy")
#     uch = data.get("uchchioy")
#     tort = data.get("tortchioy")
#     besh= data.get("beshchioy")
#     s2 = (birinchioy,ikkichioy,uch,tort,besh)
#     s=1
#     try:
#         db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
#         count = db.count_curses()[0]
#         for i in s2:
#             s+=1
#             db.add_curses_math(slog=s,oylik_reja=i,sub_id=count)
#         await message.answer("Kurs bazaga ko'shildi!")
#         await Yangi_kurs.next()
#     except:
#         await message.answer("Kurs ko'shilmadi hatolik!")


# @dp.message_handler(state=Yangi_kurs.yettichioy)
# async def get_bir(message: types.Message, state: FSMContext):
#     data= await state.get_data()
#     title = data.get("title")
#     slug = data.get("slug")
#     maney = data.get("puli")
#     malumot = data.get("malumot")
#     imge_url = data.get("imge_url")
#     birinchioy = data.get("birinchioy")
#     ikkichioy = data.get("ikkichioy")
#     uch = data.get("uchchioy")
#     tort = data.get("tortchioy")
#     besh= data.get("beshchioy")
#     olti = data.get("oltichioy")
#     s2 = (birinchioy,ikkichioy,uch,tort,besh,olti)
#     s=1
#     try:
#         db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
#         count = db.count_curses()[0]
#         for i in s2:
#             s+=1
#             db.add_curses_math(slog=s,oylik_reja=i,sub_id=count)
#         await message.answer("Kurs bazaga ko'shildi!")
#         await Yangi_kurs.next()
#     except:
#         await message.answer("Kurs ko'shilmadi hatolik!")


# @dp.message_handler(state=Yangi_kurs.sakizchioy)
# async def get_bir(message: types.Message, state: FSMContext):
#     data= await state.get_data()
#     title = data.get("title")
#     slug = data.get("slug")
#     maney = data.get("puli")
#     malumot = data.get("malumot")
#     imge_url = data.get("imge_url")
#     birinchioy = data.get("birinchioy")
#     ikkichioy = data.get("ikkichioy")
#     uch = data.get("uchchioy")
#     tort = data.get("tortchioy")
#     besh= data.get("beshchioy")
#     olti = data.get("oltichioy")
#     yetti = data.get("yettichioy")
#     s2 = (birinchioy,ikkichioy,uch,tort,besh,olti,yetti)
#     s=1
#     try:
#         db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
#         count = db.count_curses()[0]
#         for i in s2:
#             s+=1
#             db.add_curses_math(slog=s,oylik_reja=i,sub_id=count)
#         await message.answer("Kurs bazaga ko'shildi!")
#         await Yangi_kurs.next()
#     except:
#         await message.answer("Kurs ko'shilmadi hatolik!")

# @dp.message_handler(state=Yangi_kurs.tortchioy)
# async def get_bir(message: types.Message, state: FSMContext):
#     data= await state.get_data()
#     title = data.get("title")
#     slug = data.get("slug")
#     maney = data.get("puli")
#     malumot = data.get("malumot")
#     imge_url = data.get("imge_url")
#     birinchioy = data.get("birinchioy")
#     ikkichioy = data.get("ikkichioy")
#     uch = data.get("uchchioy")
#     tort = data.get("tortchioy")
#     besh= data.get("beshchioy")
#     olti = data.get("oltichioy")
#     yetti = data.get("yettichioy")
#     sakiz = data.get("sakizchioy")
#     s2 = (birinchioy,ikkichioy,uch,tort,besh,olti,yetti,sakiz)
#     s=1
#     try:
#         db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
#         count = db.count_curses()[0]
#         for i in s2:
#             s+=1
#             db.add_curses_math(slog=s,oylik_reja=i,sub_id=count)
#         await message.answer("Kurs bazaga ko'shildi!")
#         await Yangi_kurs.next()
#     except:
#         await message.answer("Kurs ko'shilmadi hatolik!")


# @dp.message_handler(state=Yangi_kurs.onchioy)
# async def get_bir(message: types.Message, state: FSMContext):
#     data= await state.get_data()
#     title = data.get("title")
#     slug = data.get("slug")
#     maney = data.get("puli")
#     malumot = data.get("malumot")
#     imge_url = data.get("imge_url")
#     birinchioy = data.get("birinchioy")
#     ikkichioy = data.get("ikkichioy")
#     uch = data.get("uchchioy")
#     tort = data.get("tortchioy")
#     besh= data.get("beshchioy")
#     olti = data.get("oltichioy")
#     yetti = data.get("yettichioy")
#     sakiz = data.get("sakizchioy")
#     toqiz = data.get("tqqizinchioy")
#     s2 = (birinchioy,ikkichioy,uch,tort,besh,olti,yetti,sakiz,toqiz)
#     s=1
#     try:
#         db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
#         count = db.count_curses()[0]
#         for i in s2:
#             s+=1
#             db.add_curses_math(slog=s,oylik_reja=i,sub_id=count)
#         await message.answer("Kurs bazaga ko'shildi!")
#         await Yangi_kurs.next()
#     except:
#         await message.answer("Kurs ko'shilmadi hatolik!")


# @dp.message_handler(state=Yangi_kurs.onbirchioy)
# async def get_bir(message: types.Message, state: FSMContext):
#     data= await state.get_data()
#     title = data.get("title")
#     slug = data.get("slug")
#     maney = data.get("puli")
#     malumot = data.get("malumot")
#     imge_url = data.get("imge_url")
#     birinchioy = data.get("birinchioy")
#     ikkichioy = data.get("ikkichioy")
#     uch = data.get("uchchioy")
#     tort = data.get("tortchioy")
#     besh= data.get("beshchioy")
#     olti = data.get("oltichioy")
#     yetti = data.get("yettichioy")
#     sakiz = data.get("sakizchioy")
#     toqiz = data.get("tqqizinchioy")
#     on = data.get("onchioy")
#     s2 = (birinchioy,ikkichioy,uch,tort,besh,olti,yetti,sakiz,toqiz,on)
#     s=1
#     try:
#         db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
#         count = db.count_curses()[0]
#         for i in s2:
#             s+=1
#             db.add_curses_math(slog=s,oylik_reja=i,sub_id=count)
#         await message.answer("Kurs bazaga ko'shildi!")
#         await Yangi_kurs.next()
#     except:
#         await message.answer("Kurs ko'shilmadi hatolik!")




# @dp.message_handler(state=Yangi_kurs.onikkichioy)
# async def get_bir(message: types.Message, state: FSMContext):
#     data= await state.get_data()
#     title = data.get("title")
#     slug = data.get("slug")
#     maney = data.get("puli")
#     malumot = data.get("malumot")
#     imge_url = data.get("imge_url")
#     birinchioy = data.get("birinchioy")
#     ikkichioy = data.get("ikkichioy")
#     uch = data.get("uchchioy")
#     tort = data.get("tortchioy")
#     besh= data.get("beshchioy")
#     olti = data.get("oltichioy")
#     yetti = data.get("yettichioy")
#     sakiz = data.get("sakizchioy")
#     toqiz = data.get("tqqizinchioy")
#     on = data.get("onchioy")
#     onbir = data.get("onikkichioy")
#     s2 = (birinchioy,ikkichioy,uch,tort,besh,olti,yetti,sakiz,toqiz,on,onbir)
#     s=1
#     try:
#         db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
#         count = db.count_curses()[0]
#         for i in s2:
#             s+=1
#             db.add_curses_math(slog=s,oylik_reja=i,sub_id=count)
#         await message.answer("Kurs bazaga ko'shildi!")
#         await Yangi_kurs.next()
#     except:
#         await message.answer("Kurs ko'shilmadi hatolik!")
    





# @dp.message_handler(state=Yangi_kurs.onikkichioy)
# async def get_bir(message: types.Message, state: FSMContext):
#     data= await state.get_data()
#     title = data.get("title")
#     slug = data.get("slug")
#     maney = data.get("puli")
#     malumot = data.get("malumot")
#     imge_url = data.get("imge_url")
#     birinchioy = data.get("birinchioy")
#     ikkichioy = data.get("ikkichioy")
#     uch = data.get("uchchioy")
#     tort = data.get("tortchioy")
#     besh= data.get("beshchioy")
#     olti = data.get("oltichioy")
#     yetti = data.get("yettichioy")
#     sakiz = data.get("sakizchioy")
#     toqiz = data.get("tqqizinchioy")
#     on = data.get("onchioy")
#     onbir = data.get("onbirchioy")
#     onikki = data.get("onikkichioy")
#     s2 = (birinchioy,ikkichioy,uch,tort,besh,olti,yetti,sakiz,toqiz,on,onbir,onikki)
#     s=1
#     try:
#         db.add_curses(title=title,slog= slug, puli=maney,malumot=malumot,imge_url=imge_url)
#         count = db.count_curses()[0]
#         for i in s2:
#             s+=1
#             db.add_curses_math(slog=s,oylik_reja=i,sub_id=count)
#         await message.answer("Kurs bazaga ko'shildi!")
#         await Yangi_kurs.next()
#     except:
#         await message.answer("Kurs ko'shilmadi hatolik!")
    







