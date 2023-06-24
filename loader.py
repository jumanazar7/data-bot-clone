from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.sqlite import Database
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database(path_to_db="C:/Users/Jumanazar/Desktop/DATA bot/DATAbot/data/main1.db")
