from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

def start_reply_keyaboard():
    builder = ReplyKeyboardBuilder()
    nav_button = KeyboardButton(text='Навигация')
    schedule_button = KeyboardButton(text='Расписание')
    question_button = KeyboardButton(text='Вопрос')
    builder.add(nav_button, schedule_button, question_button)

    return builder.as_markup(resize_keyboard=True)