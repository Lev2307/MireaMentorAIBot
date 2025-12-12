# Вариант с инлайн кнопками
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def start_inline_keyboard():
    nav_button = InlineKeyboardButton(text='Навигация', callback_data='navigation')
    schedule_button = InlineKeyboardButton(text='Расписание', callback_data='schedule')
    question_button = InlineKeyboardButton(text='Вопросик', callback_data='question')
    builder = InlineKeyboardBuilder()
    builder.add(nav_button, schedule_button, question_button)

    return builder.as_markup()