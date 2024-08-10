from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.channels import channels_markup
from filters.is_private import IsPrivateChat
from utils.misc.check_user import user_not_in_channel_urls


@dp.message_handler(IsPrivateChat(),CommandStart())
async def bot_start(message: types.Message):
    user_id = message.chat.id
    channel_urls = await user_not_in_channel_urls(user_id=user_id)
    if channel_urls:
        await message.answer("Botimizdan foydalanish uchun rasmiy kanalimizga <b>obuna bo'ling</b> va <b>Tekshirish</b> tugmasini bosing.",reply_markup=channels_markup(channel_urls))
    else:
        await message.answer("Welcom to")