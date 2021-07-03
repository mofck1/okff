import os
import asyncio
from datetime import datetime
from PIL import Image
import asyncio
from userge import Config, Message, userge
from userge.utils import get_file_id, rand_array
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

LOGGER = userge.getLogger(__name__)

@userge.on_cmd(
    "check",
    about={
        "header": "Módulo teste - @applled",
    },
    del_pre=True,
    allow_channels=False,
)

async def _apple(message: Message):
    await message.edit("**Iniciando checagem...**\nAguarde o resultado, Mestre...", log=__name__)
    photo = "https://telegra.ph/file/a9730c950f79c1f06a800.gif"
    texto = "__I'm Online, @appled!__"
    await message.client.send_animation(
                         message.chat.id, 
                         animation=photo, 
                         caption=texto,
                         reply_markup=_apple.check_buttons()
    )

        def check_buttons() -> InlineKeyboardMarkup:
        buttons = [
            [
                InlineKeyboardButton(text="TWAPPLE", url="https://t.me/twapple"),
                InlineKeyboardButton(text="BIO", url=Config.BIO_APPLE),
            ],
        ]
        return InlineKeyboardMarkup(buttons)
    
   #Adicionar outras configurações
