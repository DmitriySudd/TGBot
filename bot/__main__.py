
import asyncio
import logging
from aiogram import Bot, Dispatcher

import data
from commands import keyboard
from commands import table
from commands import commands
from commands import answer


token = '7094323356:AAG6tSBYvoTIqhqk-C0WeNXT89QpOQDTS8g'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher()
DB_NAME = 'quiz_bot.db'


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')

