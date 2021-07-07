""" Módulo de testes para o @applled com fins de aprendizado """

import os
from pyrogram.errors import YouBlockedUser
from userge import Config, Message, userge
from userge.utils.exceptions import StopConversation, progress


@userge.on_cmd("gusta", about={
    'header': "Teste do @applled",
    'como usar': "{tr}gusta"}, allow_via_bot=False)
async def gusta(msg: Message):
    chat = "/now" # msg.input_or_reply_str
    if not chat:
        await msg.err("Erro.")
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
            f"""𝐒𝐏𝐎𝐓𝐈𝐅𝐘 𝐏𝐑𝐄𝐌𝐈𝐔𝐌
            **𝙴𝚜𝚝𝚘𝚞 𝚘𝚞𝚟𝚒𝚗𝚍𝚘: [▫️]({FINAL})
            ⚡️ @applled"""
        ) # Inicio                     
            
    except YouBlockedUser: # Fim
        await msg.edit("Desbloqueie o **@SpotipieBot**")
    except StopConversation:
        await msg.err("O Bot está morto...")
