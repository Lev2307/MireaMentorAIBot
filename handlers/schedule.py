from aiogram import Router, F
from aiogram.types import CallbackQuery


schedule_router = Router()

@schedule_router.callback_query(F.data == 'schedule')
async def schedule_answer(callback_query: CallbackQuery):
    await callback_query.message.answer('Я пока только учусь')