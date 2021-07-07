""" Módulo de testes para o @applled com fins de aprendizado """

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
#   chat_id = message.chat.id
    bott = FINAL
    if not chat:
#        await msg.err("@applled")
#        return
        await message.err("@applled") # t
    bot = await userge.bot.get_me()
    x = await userge.get_inline_bot_results(
        bot.username, "{final} 𝐒𝐏𝐎𝐓𝐈𝐅𝐘 𝐏𝐑𝐄𝐌𝐈𝐔𝐌"
    ) # t
    try:
        async with userge.conversation("SpotipieBot") as conv:
            await conv.send_message("/start")
            await conv.get_response(mark_read=True)
            await conv.send_message(chat)
            final = (
                await conv.get_response(mark_read=True)
            )
#        await msg.edit(
#            f"𝐒𝐏𝐎𝐓𝐈𝐅𝐘 𝐏𝐑𝐄𝐌𝐈𝐔𝐌\n {FINAL}") 
            await userge.send_inline_bot_result(
#       chat_id=message.chat.id,
        query_id=x.query_id,
        result_id=x.results[0].id,
        bott=FINAL
    )
    except YouBlockedUser: 
        await msg.edit("Desbloqueie o **@SpotipieBot**")
    except StopConversation:
        await msg.err("O Bot está morto...")
