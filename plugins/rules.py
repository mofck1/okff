""" Mรณdulo de testes para o @applled com fins de aprendizado """
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
   "!warn You know the /rules and so do I ๐ต",
)
RULES_FINAL = (
   "[๐๐๐ ๐๐๐๐  ๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐ ๐๐ ๐ธ](https://www.youtube.com/watch?v=dQw4w9WgXcQ) ๐ต",
)
ANIMTN = (
    "https://telegra.ph/file/7465c70c1cb0f35cc536e.gif",
)

@userge.on_cmd(
    "rules$", about={"header": "Mรณdulo teste para o @applled"}, trigger="", allow_via_bot=False
)

async def regras(message: Message):
    await message.edit(f"{random.choice(RULES)}", del_in=5, log=__name__)
    photo = f"""{random.choice(ANIMTN)}"""
    texto = f"""{random.choice(RULES_FINAL)}"""
    await message.client.send_animation(
                         message.chat.id, 
                         animation=photo, 
                         caption=texto,
    )
