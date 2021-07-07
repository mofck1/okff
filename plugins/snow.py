""" Módulo de testes para o @applled com fins de aprendizado """
""" Sua exibição ainda está em testes """
import asyncio
import os
from pyrogram.errors import YouBlockedUser
from userge import Config, Message, userge
from userge.utils.exceptions import StopConversation


@userge.on_cmd("snow", about={
    'header': "Teste do @applled",
    'como usar': "{tr}snow"}, allow_via_bot=False, allow_channels=False,)

async def gusta(msg: Message):
    chat = "/now" # msg.input_or_reply_str
    chat_id = msg.chat.id
    if not chat:
        await msg.err("@applled")
        return
    try:
        async with userge.conversation("SpotipieBot") as conv:
            await conv.send_message("/start")
            await conv.get_response(mark_read=True)
            await conv.send_message(chat)
            FINAL = (
                await conv.get_response(mark_read=True)
            )    
        await msg.edit(
            f"𝐒𝐏𝐎𝐓𝐈𝐅𝐘 𝐏𝐑𝐄𝐌𝐈𝐔𝐌\n {FINAL}") 
    except YouBlockedUser: 
        await msg.edit("Desbloqueie o **@SpotipieBot**")
    except StopConversation:
        await msg.err("O Bot está morto...")
