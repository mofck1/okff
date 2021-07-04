""" Trabalhar no port do módulo """


import os
import time

import requests
import ujson
from pyrogram.errors.exceptions.bad_request_400 import AboutTooLong, FloodWait, YouBlockedUser

from userge import Config, Message, get_collection, userge

from asyncio.exceptions import TimeoutError

from userge import Config, Message, userge
from userge import DOWN_PATH, bot
from userge.events import register

@userge.on_cmd("sfy", about={"header": "Teste de Port",},
    del_pre=True,
    allow_channels=False,
)

async def fy_(message: Message):
    chat = "@SpotifyNowBot"
    now = "/now"
    await message.edit("**Processando...**")
    try:
        async with userge.conversation(chat) as conv:
            try:
                msg = await conv.send_message(now)
                response = await conv.get_response()
                """ - don't spam notif - """
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await message.reply("**Por favor desbloqueie** @SpotifyNowBot**.**")
                return
            if response.text.startswith("You're"):
                await message.edit(
                    "**Você não está ouvindo nada no Spotify no momento.**"
                )
                return
            downloaded_file_name = await event.client.download_media(
                response.media, DOWN_PATH
            )
            link = response.reply_markup.rows[0].buttons[0].url
            await message.client.send_file(
                message.chat_id,
                downloaded_file_name,
                force_document=False,
                caption=f"[Tocar no Spotify]({link})",
            )
            """ - cleanup chat after completed - """
            await message.client.delete_messages(conv.chat_id, [msg.id, response.id])
    except TimeoutError:
        return await message.edit("**Erro:** @SpotifyNowBot **não está respondendo.**")
    await message.delete()
    return os.remove(downloaded_file_name)

