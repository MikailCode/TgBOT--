import asyncio
from aiogram import Dispatcher, Bot
from handler import rt

async def main():
	dp = Dispatcher()
	bot = Bot(token='TOKEN')
	dp.include_router(rt)
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())