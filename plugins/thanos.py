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

FBAN = (
   "<i>Já leu as mensagens fixadas? Se tá lendo isso, você não é cego.</i>",
)
THANOSSAID = (
   "<i>Perfectly balanced, as all things should be.</i>\nMensagens Importantes: [#1](https://t.me/redminote8br/1879553) / [#2](https://t.me/redminote8br/1869155)",
)
THANOS = (
    "https://telegra.ph/file/93a2f322f395bf0f8d66b.gif",
)

@userge.on_cmd(
    "leia$", about={"header": "Módulo teste para o @applled"}, trigger="", allow_via_bot=False
)

async def regras(message: Message):
    await message.edit(f"{random.choice(FBAN)}", del_in=5, log=__name__)
    photo = f"""{random.choice(THANOS)}"""
    texto = f"""{random.choice(THANOSSAID)}"""
    await message.client.send_animation(
                         message.chat.id, 
                         animation=photo, 
                         caption=texto,
    )
