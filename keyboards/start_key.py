from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup
from config_reader import config
from typing import Optional

# Создаем базовую клавиатуру
def get_start_keyboard(user_id: Optional[int] = None) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.button(text='📌Добавить закладку📌')
    builder.button(text='📚Мои закладки📚')
    builder.button(text='📋Самые популярные теги📋')

    if user_id == int(config.admin_id.get_secret_value()):
        builder.button(text='Админ панель')

    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)



