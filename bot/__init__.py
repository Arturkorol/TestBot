from aiogram import Dispatcher

from .routers.navigation import router as navigation_router

__all__ = ["dp"]

# Main application dispatcher
dp = Dispatcher()
dp.include_router(navigation_router)
