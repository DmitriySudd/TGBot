import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=os.getenv('token'))
    dp = Dispatcher()

    @dp.message(Command('start'))
    async def cmd_start(message: types.Message) -> None:
        await message.answer('Привет! Я твой новый бот.')

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')

