from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards.start_key import get_start_keyboard
from keyboards.info_callback_key import InfoCallbackFactory, get_InfoCallback


router = Router()

# Хэндлер обработки кнопки Добавить закладку
@router.message(F.text == "📌Добавить закладку📌")
async def handle_Bookmark(message: Message):
    await message.answer(
        'Это пока заглушка добавления закладок',
        reply_markup=get_start_keyboard(message.from_user.id))

# Хэндлер обработки кнопки Мои закладки
@router.message(F.text == "📚Мои закладки📚")
async def handle_getMyBookmark(message: Message):
    await message.answer(
        'Это пока заглушка моих закладок',
        reply_markup=get_start_keyboard(message.from_user.id))

# Хэндлер обработки кнопки Самые популярные теги
@router.message(F.text == "📋Самые популярные теги📋")
async def handle_getRankedBookmark(message: Message):
    await message.answer(
        'Это пока заглушка самых популярных тегов',
        reply_markup=get_start_keyboard(message.from_user.id))

@router.message(Command('Info'))
async def cmd_getInfo(message: Message):
    await message.answer('ℹ️Что-то непонятно? Спрашивайте...ℹ️', reply_markup=get_InfoCallback())

# Хэндлер обработки кнопки информационного табло
@router.callback_query(InfoCallbackFactory.filter()) # фильтруем только информационные колбэки
async def handle_INFO(callback: CallbackQuery, callback_data: InfoCallbackFactory):
    pass
