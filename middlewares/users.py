from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update
from utils.misc.check_user import user_not_in_channel_urls
from aiogram.dispatcher.handler import CancelHandler
from keyboards.inline.channels import channels_markup

class SimpleMiddleware(BaseMiddleware):
    
    async def on_pre_process_update(elf, update: Update, data: dict):
        if update.message:
            if update.message.text in ("/help","/start"):
                return
            user_id = update.message.chat.id
            channel_urls = await user_not_in_channel_urls(user_id)
            if channel_urls:
                await update.message.answer("Barcha kanallarga obuna bo'ling",reply_markup=channels_markup(channel_urls))
                raise CancelHandler()
            else:
                return
            
            