from aiogram import Router
from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.exceptions import TelegramBadRequest


from templates_text import hello_message, \
                           help_message

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=hello_message(message.from_user.full_name))


@router.message(Command("help", prefix='!/'))
async def handle_help(message: types.Message):
    await message.answer(text=help_message())






