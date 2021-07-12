""" Módulo de testes para o @applled com fins de aprendizado  """

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

@userge.on_cmd(
    "checking",
    about={
        "header": "Módulo teste para o @applled",
    },
    del_pre=True,
    allow_channels=False,
    allow_via_bot=True,
)

async def apple(message: Message):
    await message.edit("**𝚃𝚎𝚜𝚝𝚎 𝚐𝚎𝚛𝚊𝚍𝚘...**\n𝙰𝚐𝚞𝚊𝚛𝚍𝚎 𝚘 𝚛𝚎𝚜𝚞𝚕𝚝𝚊𝚍𝚘, 𝙼𝚎𝚜𝚝𝚛𝚎...", del_in=1, log=__name__)
    texto = "@applled"
    mediag = await userge.bot.get_messages("orugugu", 61)
    media_id = get_file_id(mediag)  
    await userge.send_inline_bot_result(
                         media=media_id,
                         message.chat.id, 
                         caption=texto,
    )
