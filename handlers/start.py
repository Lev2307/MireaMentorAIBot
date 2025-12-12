from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.inline_keyboards import start_inline_keyboard

start_router = Router()

@start_router.message(Command('start'))
async def start(message: Message):
    await message.answer("Привет, я AI-ассистент РТУ МИРЭА 🤖. Чем могу помочь?", reply_markup=start_inline_keyboard())