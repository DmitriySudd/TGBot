from aiogram.filters.command import Command
from aiogram import Bot, types, Dispatcher


@dp.message(Command('start'))
async def cmd_start(message: types.Message) -> None:
    await message.answer('Привет! Я твой новый бот.')