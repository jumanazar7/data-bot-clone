from aiogram.dispatcher.filters.state import StatesGroup,State

class ustoz(StatesGroup):
    title = State()
    slog = State()
    tajribasi = State()
    image_url = State()
    sub_curses_id = State() 
    tugatish = State()

class royhat_sate(StatesGroup):
    ism = State()
    curs = State()
    ha = State()


class back_to_video(StatesGroup):
    curses = State()
    video = State()
    reja = State()
class insert_to_video(StatesGroup):
    fan  = State()
    sub_id = State()
    slug = State()
    malumot = State()
    reja = State()   

class Cursstate(StatesGroup):
    curses = State()
    ustozlar = State()
    reja = State()
    
class Cursstate1(StatesGroup):
    curses = State()
    ustozlar = State()
    reja = State()
    

class murojat(StatesGroup):
    oy = State()

class delete_ustoz(StatesGroup):
    ochir = State()


class delete_state(StatesGroup):
    ochir = State()

class Yangi_kurs(StatesGroup):
    birinchioy=State()
    ikkichioy =State()
    uchchioy=State()
    tortchioy=State()
    beshchioy=State()
    oltichioy=State()
    yettichioy=State()
    sakizchioy=State()
    tqqizinchioy=State()
    onchioy=State()
    onbirchioy=State()
    onikkichioy=State()
    tugadi = State()
    tugadi1 = State()

    
class Yangi_kurs_1(StatesGroup):
    title = State()
    slug = State()
    maney = State()
    malumot = State()
    imge_url = State()
    birinchioy=State()
    ikkichioy =State()
    uchchioy=State()
    tortchioy=State()
    beshchioy=State()
    oltichioy=State()
    yettichioy=State()
    sakizchioy=State()
    tqqizinchioy=State()
    onchioy=State()
    onbirchioy=State()
    onikkichioy=State()
    tugadi = State()

class ustozlar(StatesGroup):
    title = State()
    slug = State()
    tajribasi = State()
    imge_url = State()
    qaysi_yon = State()

class reklama(StatesGroup):
    birinchi=State()
    suratli=State()
    suratsz=State()
    vidio=State()
    Voice=State()