from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from keyboards.start_key import get_start_keyboard

router = Router()

# Создаем стартовый хэндлер
@router.message(Command('start'))
async def handle_start(message: Message):
    await message.answer(
        "🖐️Добро пожаловать!🖐️\n"
        "🤫Пожалуйста, не шумите в библиотеке🤫\n"
        "За справкой обратитесть сюда: <a href='/Info'>/Info</a>", # <a href='/Info'>/Info</a> - делает кликабельной команду /Info
        parse_mode=ParseMode.HTML,
        reply_markup=get_start_keyboard(message.from_user.id)
    )