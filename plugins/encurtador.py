""" Módulo de testes para o @applled com fins de aprendizado """

import os
import asyncio
import requests
import json
from userge import Config, Message, userge
import gdshortener

from pyrogram.errors import YouBlockedUser
from userge.utils import get_file_id, rand_array

@userge.on_cmd(
    "url",
    about={
        "header": "Módulo teste para o @applled",
    },
    del_pre=True,
    allow_channels=False,
)
 
    async def is_gd(message: Message):
    url = msg.input_or_reply_str
    if not url:
        await msg.err("Hello?! Precisa de uma url.")
        return
    s = gdshortener.ISGDShortener()
    try:
        s_url, stats = s.shorten(url, log_stat=True)
    except Exception as er:
        await msg.err(str(er))
    else:
        await msg.edit(
            f"**URL Encurtada:**\n`{s_url}`\n\n**Stats:** `{stats}`",
            disable_web_page_preview=True,
        )
    
