""" Módulo de testes para o @applled com fins de aprendizado """

import asyncio
import os
from pyrogram.errors import YouBlockedUser
from userge import Config, Message, userge
from userge.utils.exceptions import StopConversation


@userge.on_cmd("arq", about={
    'header': "Teste do @applled",
    'como usar': "{tr}arq"}, allow_via_bot=False, allow_channels=False,)

async def arquivo(msg: Message):
    chat = msg.input_or_reply_str
    if not chat:
        await msg.err("@applled")
        return
    try:
        async with userge.conversation("uploadbot") as conv:
            await conv.send_message("/start")
            await conv.get_response(mark_read=True)
            await conv.send_message(chat)
            UPLOAD = (
                await conv.get_response(mark_read=True)
            )
        await msg.edit(
            f"Teste\n {UPLOAD}") 
    except YouBlockedUser: 
        await msg.edit("Desbloqueie o **@uploadbot**")
    except StopConversation:
        await msg.err("O Bot está morto...")
