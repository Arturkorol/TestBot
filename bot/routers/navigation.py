from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Handle the /start command."""
    await message.answer("Welcome to the bot!")


@router.message(Command("menu"))
async def cmd_menu(message: Message) -> None:
    """Display the main navigation menu."""
    await message.answer("This is the main menu.")
