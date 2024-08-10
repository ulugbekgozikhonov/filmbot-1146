from loader import dp
from aiogram import types
from utils.misc.check_user import user_not_in_channel_urls

@dp.callback_query_handler(text="tekshir")
async def check_handler(call: types.CallbackQuery):
    user_id = call.message.chat.id
    
    channel_urls = await user_not_in_channel_urls(user_id=user_id)
    if channel_urls:
        await call.answer(text="Kanalga hali obuna bo'lmagansiz⚠️",show_alert=True)
    else:
        await call.message.edit_text(text="Film codini yuboring...")
    
    
    