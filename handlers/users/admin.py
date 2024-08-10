from loader import dp
from aiogram import types

from filters.is_admin import IsAdmin

@dp.message_handler(IsAdmin(), commands=['addfilm'])
async def add_film_handler(message: types.Message):
    await message.answer("Film qo'shishingiz mumkin")