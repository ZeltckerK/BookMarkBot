from aiogram import Router, F
from aiogram.types import Message
from keyboards.start_key import get_start_keyboard


router = Router()

# Хэндлер обработки кнопки
@router.message(F.text)
async def handle_bookmark(message: Message):
    await message.answer(
        'Это текст',
        reply_markup=get_start_keyboard(message.from_user.id))
