from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils import executor

API_TOKEN = '6626086371:AAHYxRs7aOFn1p_NawCyVPcMV2Yg1Q3RKUI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Start Game", web_app=WebAppInfo(url="https://github.com/emilki/PotatoCoin.git")))
    await message.reply("Welcome to Potato Clicker! Click the button below to start the game.", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
