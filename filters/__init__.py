from loader import dp
from .is_private import IsPrivateChat
from .is_admin import IsAdmin


if __name__ == "filters":
    dp.filters_factory.bind(IsPrivateChat)
    dp.filters_factory.bind(IsAdmin)
