from aiogram import Router

router = Router()

@router.message()
async def hello(message):
    await message.answer(f"Hello {message.from_user.first_name}")