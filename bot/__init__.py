from aiogram import Dispatcher

from .routers import request as request_router
from .utils import generate_request_pdf, send_email

# Dispatcher instance used by the application
dispatcher = Dispatcher()
dispatcher.include_router(request_router.router)

__all__ = ["dispatcher", "generate_request_pdf", "send_email"]
