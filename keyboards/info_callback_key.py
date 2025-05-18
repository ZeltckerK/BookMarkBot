'''
Здесь будет реализована коллбэк логика для информационного табло
'''

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

# Класс фабрики для информационного табло
class InfoCallbackFactory(CallbackData, prefix='info'):
    doing: str # отображает какая именно справка должна быть получена пользователем


def get_InfoCallback():
    builder = InlineKeyboardBuilder()
    builder.button(text='❓Добавить закладку❓', callback_data=InfoCallbackFactory(doing='add'))
    builder.button(text='❓Мои закладки❓', callback_data=InfoCallbackFactory(doing='myMark'))
    builder.button(text='❓Самые популярные теги❓', callback_data=InfoCallbackFactory(doing='rating'))

    builder.adjust(2)

    return builder.as_markup()