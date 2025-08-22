from aiogram.fsm.context import FSMContext
from aiogram.types import Message


async def reset_to_menu(message: Message, state: FSMContext) -> None:
    """Clear the current state and notify the user about returning to the menu."""
    await state.clear()
    await message.answer("Вы вернулись в главное меню.")
