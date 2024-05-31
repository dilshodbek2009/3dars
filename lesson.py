from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from state import AddUserState
from button import main_menu, next_menu
from data import db

storage = MemoryStorage()

BOT_TOKEN = "6933405131:AAGddKCkVS7xo-M1qk0Z48CRQzsafcSryGY"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands="start")
async def start_bot(message: types.Message):
    await message.answer("Botga xush kelibsan ukam",
                         reply_markup=main_menu())


@dp.message_handler(Text(equals="User"))
async def start_bot(message: types.Message):
    await message.answer("Botga xush kelibsan ukam",
                         reply_markup=next_menu())


@dp.message_handler(Text(equals="Product"), state=None)
async def start_bot(message: types.Message):
    await message.answer("nomini kiriting",
                         reply_markup=ReplyKeyboardRemove())
    await AddUserState.title.set()


@dp.message_handler(state=AddUserState.title)
async def start_bot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await message.answer("malumot kiriting")
    await AddUserState.next()


@dp.message_handler(state=AddUserState.text)
async def start_bot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await message.answer("Narxini kiriting")
    await AddUserState.next()


@dp.message_handler(state=AddUserState.price)
async def start_bot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await message.answer("manzilni kiriting")
    await AddUserState.next()


@dp.message_handler(state=AddUserState.country)
async def start_bot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['country'] = message.text
    await message.answer("rasmini kiriting")
    await AddUserState.next()


@dp.message_handler(state=AddUserState.photo, content_types="photo")
async def start_bot(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[- 1].file_id

    await state.finish()
    await message.answer_photo(photo=data['photo'],
                               caption=f"nomi{data['name']} haqida malumot {data['text']}\n"
                                       f"narxi {data['price']} {data['country']}da ishlab chiqarilgan")


if __name__ == '__main__':
    executor.start_polling(dp)
