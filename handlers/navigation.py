from aiogram import Router, F
from aiogram.types import CallbackQuery


nav_router = Router()

@nav_router.callback_query(F.data == 'navigation')
async def navigation_answer(callback_query: CallbackQuery):
    await callback_query.message.answer('Я пока только учусь')