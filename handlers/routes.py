from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Hello {message.from_user.first_name}")

@router.message(Command("random"))
async def random(message: Message):
    await message.answer(f"This is a randon fact")

@router.message(Command("gpt"))
async def gpt(message: Message):
    await message.answer(f"This is a gpt")

@router.message(Command("talk"))
async def talk(message: Message):
    await message.answer(f"This is a talk")

@router.message(Command("quiz"))
async def quiz(message: Message):
    await message.answer("This is a quiz")


@router.message()
async def messages(message: Message):
    await message.answer("<b>Some text</b>", parse_mode="HTML")