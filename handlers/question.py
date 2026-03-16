from datetime import datetime

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import pytz

from search.search_engine import search
from search.helpers import get_possible_options, save_requests

question_router = Router()

class Question(StatesGroup):
    name = State()
    
@question_router.callback_query(F.data == 'question')
async def question_answer(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Question.name)
    await callback_query.message.edit_text('Задайте интересующий Вас вопрос... 💬')

@question_router.message(Question.name)
async def proccess_question(message: Message, state: FSMContext):
    question = message.text
    possible_options = await get_possible_options()
    search_results = await search(question, possible_options)
    for i in search_results:
        await message.answer(i['answer'])
    
    for res in search_results:
        res["timestamp"] = datetime.now(tz=pytz.timezone("Europe/Moscow")).replace(microsecond=0).isoformat()
        res['matched'] = True if res['score'] > 0 else False
        await save_requests(res)
    await state.clear()
