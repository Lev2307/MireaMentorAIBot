import os
import logging
import sys
import asyncio
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv

from handlers.start import start_router
from handlers.navigation import nav_router
from handlers.schedule import schedule_router
from handlers.question import question_router

load_dotenv()

dp = Dispatcher()

async def main():
    bot = Bot(token=os.environ.get("BOT_TOKEN"))
    dp.include_routers(start_router, nav_router, schedule_router, question_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())