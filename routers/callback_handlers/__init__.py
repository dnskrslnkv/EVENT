from aiogram import Router
from .callback_query_handlers import router as info_kb_callback_router

router = Router(name=__name__)

router.include_router(info_kb_callback_router)