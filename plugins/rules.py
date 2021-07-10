""" Módulo de testes para o @applled com fins de aprendizado """
import os
import asyncio
from datetime import datetime
from PIL import Image
import asyncio
import random
from userge import Config, Message, userge
from userge.utils import get_file_id, rand_array
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

LOGGER = userge.getLogger(__name__)

RULES = (
   "!warn You know the /rules and so do I [🎵](https://www.youtube.com/watch?v=dQw4w9WgXcQ)",
)
ANIMTN = (
    "https://telegra.ph/file/7465c70c1cb0f35cc536e.gif",
)

@userge.on_cmd(
    "rules",
    about={
        "header": "Módulo teste para o @applled",
    },
    del_pre=True,
    allow_channels=False,
)

async def regras(message: Message):
#   await message.edit("**Oh no...", del_in=1, log=__name__)
    photo = f"""{random.choice(ANIMTN)}"""
    texto = f"""{random.choice(RULES)}"""
    await message.client.send_animation(
                         message.chat.id, 
                         animation=photo, 
                         caption=texto,
    )
