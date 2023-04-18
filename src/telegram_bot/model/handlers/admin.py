from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from model.filters.admin import AdminFilter
from model.template.templates import RenderTemplate
from model.keyboards.menu_buttons import menu_keyboard

render = RenderTemplate()

admin_router = Router()
headers = {"throttling_key": "default", "long_operation": "typing"}
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart(), flags=headers)
async def admin_start(message: Message):
    await message.reply("Доп права2!", reply_markup=menu_keyboard)


