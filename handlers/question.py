from aiogram import Router, F
from aiogram.types import CallbackQuery

question_router = Router()

@question_router.callback_query(F.data == 'question')
async def question_answer(callback_query: CallbackQuery):
    await callback_query.message.answer('Я пока только учусь')