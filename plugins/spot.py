""" Módulo de testes para o @applled com fins de aprendizado """
""" Sua exibição ainda está em testes """

import asyncio
import os
from pyrogram.errors import YouBlockedUser
from userge import Config, Message, userge, DOWN_PATH
from userge.utils.exceptions import StopConversation

from .conversation import Conversation
from .send_read_acknowledge import SendReadAcknowledge

@userge.on_cmd("spot", about={
    'header': "Teste do @applled",
    'como usar': "{tr}spot"}, # allow_via_bot=False, allow_channels=False,
              )

async def gustavo(msg: Message)::
    chat = "@spotipiebot"
    now = "/now"
    await msg.edit("**Processando...**")
    try:
        async with msg.client.conversation(chat) as conv:
            try:
                msg = await conv.send_message(now)
                response = await conv.get_response()
                """ - don't spam notif - """
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await msg.reply("**Por favor desbloqueie** @spotipiebot**.**")
                return
            if response.text.startswith("You're"):
                await msg.edit(
                    "**Você não está ouvindo nada no Spotify no momento.**"
                )
                return
            downloaded_file_name = await msg.client.download_media(
                response.media, DOWN_PATH
            )
            link = response.reply_markup.rows[0].buttons[0].url
            await msg.client.send_file(
                msg.chat_id,
                downloaded_file_name,
                force_document=False,
                caption=f"[Tocar no Spotify]({link})",
            )
            """ - cleanup chat after completed - """
            await msg.client.delete_messages(conv.chat_id, [msg.id, response.id])
    except TimeoutError:
        return await msg.edit("**Erro:** @spotipiebot **não está respondendo.**")
    await msg.delete()
    return os.remove(downloaded_file_name)
