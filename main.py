'''
main.py является точкой входа в бота. Здесь инициализирован сам бот,
диспетчер, логгирование, запущен поллинг, зарегестрированы роутеры.
'''

import asyncio
import logging

from aiogram import Dispatcher, Bot

from config_reader import config
from handlers import (start_handler, user_handlers, default_handler)

routers = [start_handler.router, user_handlers.router, default_handler.router]

async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(*routers) #распаковываем и инициализируем роутеры

    logging.basicConfig(level=logging.INFO)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())