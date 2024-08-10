from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


def channels_markup(channel_urls: list):
    markup = InlineKeyboardMarkup()
    
    for i,url in enumerate(channel_urls):
        btn = InlineKeyboardButton(text=f"{i+1}-kanal",url=url)
        markup.add(btn)
        
    markup.add(InlineKeyboardButton(text="✅Tekshirish",callback_data="tekshir"))
    
    return markup