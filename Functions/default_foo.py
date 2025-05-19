'''
Функция выдающая ссылку на справку для пользователей, которые заблудились в боте
'''


from aiogram.types import Message
from aiogram.enums import ParseMode

from keyboards.start_key import get_start_keyboard

async def default_function(message: Message):
    await message.answer(
        'Для справки о командах тык сюда -> <a href="/Info">/Info</a>',
        parse_mode=ParseMode.HTML,
        reply_markup=get_start_keyboard(message.from_user.id))