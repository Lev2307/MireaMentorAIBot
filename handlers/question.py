from datetime import datetime

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import pytz
import yaml

question_router = Router()

class Question(StatesGroup):
    name = State()

async def get_possible_keywords() -> dict:
    with open('testdata/faq.yaml', encoding='utf-8', mode='r') as f:
        config_data = yaml.safe_load(f)
        return config_data['data']
    
async def save_requests(question: str, answer: str, time: datetime):
    with open('logs/requests.log', encoding='utf-8', mode='a') as f:
        f.write(f"Вопрос: {question}\nОтвет: {answer}\nВремя запроса: {time}\n\n")

@question_router.callback_query(F.data == 'question')
async def question_answer(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Question.name)
    await callback_query.message.edit_text('Задайте интересующий Вас вопрос... 💬')

@question_router.message(Question.name)
async def proccess_question(message: Message, state: FSMContext):
    question = message.text
    time, answer = datetime.now(tz=pytz.timezone("Europe/Moscow")), 'Не знаю, попробуй переформулировать'
    possible_options = await get_possible_keywords()
    flag = False
    for option in possible_options:
        matches = [i for i in option['keywords'] if i in question.split()]
        if matches:
            flag = True
            answer = option['answer']
            await message.answer(answer)
    if not flag:
        await message.answer(answer)
    await save_requests(question, answer, time)
    await state.clear()
