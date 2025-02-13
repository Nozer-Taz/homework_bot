from decouple import config
from aiogram import Dispatcher, Bot, executor, types
import logging


token = config('TOKEN')

bot = Bot(token=token)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(chat_id=message.from_user.id, text=f'Hello {message.from_user.first_name}\n Your telegram id - {message.from_user.id}')
    await message.answer('Hello!')

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)