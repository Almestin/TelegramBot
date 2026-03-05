from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(f"Hello {message.from_user.first_name}")

@router.message()
async def messages(message: Message):
    await message.answer("<b>Some text</b>", parse_mode="HTML")