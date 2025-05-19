from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from keyboards.start_key import get_start_keyboard

from Functions.default_foo import default_function

router = Router()

user_id = [] # заглушка id пользователей(здесь должна быть БД)

# Создаем стартовый хэндлер
@router.message(Command('start'))
async def handle_start(message: Message):
    if message.from_user.id in user_id:
        await default_function(message)
        return

    user_id.append(message.from_user.id)

    await message.answer(
        "🖐️Добро пожаловать!🖐️\n"
        "🤫Пожалуйста, не шумите🤫\n"
        "За справкой обратитесть сюда: <a href='/Info'>/Info</a>", # <a href='/Info'>/Info</a> - делает кликабельной команду /Info
        parse_mode=ParseMode.HTML,
        reply_markup=get_start_keyboard(message.from_user.id)
    )