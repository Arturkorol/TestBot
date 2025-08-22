from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.utils.reset import reset_to_menu

router = Router()


@router.message(Command("menu"))
async def show_menu(message: Message, state: FSMContext) -> None:
    """Handler to reset state and show the main menu."""
    await reset_to_menu(message, state)
