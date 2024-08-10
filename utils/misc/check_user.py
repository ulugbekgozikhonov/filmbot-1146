from data.config import CHANNELS
from loader import bot

async def user_not_in_channel_urls(user_id):
    
    channels = []
    
    for channel_id, channel_url in CHANNELS.items():
        
        member = await bot.get_chat_member(chat_id=channel_id,user_id=user_id)
        
        if member.status in ("administrator","member","creator","owner"):
            continue
        else:
            channels.append(channel_url)
    
    return channels
        