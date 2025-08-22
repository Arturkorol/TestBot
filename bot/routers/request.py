from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from ..states import RequestStates
from ..utils import generate_request_pdf, send_email

router = Router()


@router.message(Command("request"))
async def start_request(message: Message, state: FSMContext) -> None:
    """Entry point for the /request command."""

    await message.answer("Please enter your request text.")
    await state.set_state(RequestStates.waiting_for_request)


@router.message(RequestStates.waiting_for_request)
async def handle_request_text(message: Message, state: FSMContext) -> None:
    """Receive the request text, generate a PDF and send it via e-mail."""

    pdf_bytes = await generate_request_pdf(message.text)
    await send_email(pdf_bytes)
    await message.answer("Your request has been sent. Thank you!")
    await state.clear()
