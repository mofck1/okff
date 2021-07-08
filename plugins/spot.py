""" Módulo de testes para o @applled com fins de aprendizado """
""" Sua exibição ainda está em testes """

import asyncio
import os
from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from userge import Config, Message, userge
from userge.utils.exceptions import StopConversation

from userge.core.methods.chats import Conversation 
from userge.core.methods.chats import SendReadAcknowledge

@userge.on_cmd("spot", about={
    'header': "Teste do @applled",
    'como usar': "{tr}spot"},  allow_via_bot=False, allow_channels=False,
              )

async def spott(msg: Message):
    chat = "@SpotifyNowBot"
    now = "/now"
    await msg.edit("**Processando...**")
    try:
        async with msg.client.conversation(chat) as conv:
            try:
                msg = await conv.send_message(now)
                response = await conv.get_response()
                """ - don't spam notif - """
                await client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUser:
                await message.reply("**Por favor desbloqueie** @SpotifyNowBot**.**")
                return
            if response.text.startswith("You're"):
                await message.edit(
                    "**Você não está ouvindo nada no Spotify no momento.**"
                )
                return
            downloaded_file_name = await message.client.download_media(
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
            await msg.client.delete_messages(conv.chat_id, [msg.id, response.id])
    except TimeoutError:
        return await msg.edit("**Erro:** @SpotifyNowBot **não está respondendo.**")
    await msg.delete()
    return os.remove(downloaded_file_name)
