'''
Все не обрабатываемые запросы летят сюда
'''

from aiogram import Router
from aiogram.types import Message

from Functions.default_foo import default_function

router = Router()

@router.message()
async def default_handler(message: Message):
    await default_function(message)