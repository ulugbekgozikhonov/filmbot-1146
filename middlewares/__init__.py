from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .users import SimpleMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(SimpleMiddleware())
