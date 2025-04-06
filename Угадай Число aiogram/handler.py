from aiogram import types, Router, F
from aiogram.filters import Command
import random
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

rt = Router()

num = []

class Ugadai(StatesGroup):
	number = State()

@rt.message(Command('lol'))
async def start(mes: types.Message, state: FSMContext):
	num.append(str(random.randint(1, 10)))
	await state.set_state(Ugadai.number)
	if len(num) >= 2:
		del num[0]
	await mes.answer('Я загадал число, сможешь отгадать? Напиши число')

@rt.message(Ugadai.number)
async def number(mes: types.Message, state: FSMContext):
	await state.update_data(number=num)
	data = await state.get_data()
	if mes.text in data['number']:
		await mes.answer('Ты угадал, молодец.\n\nЧтобы сыграть еще раз, введи команду /start')
		await state.clear()
	elif int(mes.text) > 10 or int(mes.text) <= 0:
		await mes.answer('Число не находится в диапазоне от 1 до 10')
	else:
		await mes.answer('Не угадал, попробуй еще раз')
		print(num)