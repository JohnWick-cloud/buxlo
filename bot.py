import logging
from aiogram import Bot, Dispatcher, executor, types
import cfg
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import random
from text import all_text

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=cfg.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

button_next = KeyboardButton('Следующее')
kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_next)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Следующее', reply_markup=kb1)

@dp.message_handler(text='Следующее')
async def next(message: types.Message):
    await message.answer(random.choice(all_text), reply_markup=kb1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
