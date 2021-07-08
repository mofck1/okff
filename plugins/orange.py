""" Módulo de testes para o @applled com fins de aprendizado """
""" Sua exibição ainda está em testes """

import asyncio
import os
from pyrogram.errors import YouBlockedUser

from userge import Config, Message, userge
from userge.utils.exceptions import StopConversation

@userge.on_cmd(
    "oran",
    about={
        "header": "TESTE",
        "flags": {"-l": "limit, for multiple messages"},
        "usage": "Reply {tr}oran",
        "examples": ["{tr}oran"],
    },
    allow_via_bot=False,
    del_pre=True,
)
async def orangemd(message: Message):
    """orangecmd"""
    chat = "/now"
    fy_list = []
    self_mid = False
    args = ""
    if chat:
        if "l" in message.flags:
            limit = message.flags.get("l", 1)
            if not limit.isdigit():
                await message.err("give valid no. of message to quote", del_in=5)
                return
            num_ = min(int(limit), 24)
            async for msg in userge.iter_history(
                message.chat.id, limit=num_, offset_id=chat.message_id, reverse=True
            ):
                if msg.message_id != message.message_id:
                    fy_list.append(msg.message_id)
            if message.filtered_input_str:
                self_mid = True
                await message.edit(message.filtered_input_str)
        else:
            fy_list.append(message.message_id)
            if message.input_str:
                self_mid = True
                await message.edit(message.input_str)
    else:
        args = message.input_str
    if self_mid:
        fy_list.append(message.message_id)
    else:
        await message.delete()
    if not args and len(quote_list) == 0:
        await message.err("ZZZZZZZZZZ !", del_in=5)
        return
    try:
        async with userge.conversation("spotipiebot", timeout=100) as conv:
            try:
                if fy_list:
                    await userge.forward_messages(
                        "spotipiebot", message.chat.id, fy_list
                    )
                    if self_mid:
                        await message.delete()
                elif args:
                    await conv.send_message(args)
            except YouBlockedUser:
                await message.edit("first **unblock** @spotipiebot")
                return
            fyfy = await conv.get_response(mark_read=True)
            if not (fyfy.arquivo or fyfy.document):
                await message.err("something went wrong!")
                return
            message_id = chat.message_id if chat else None
            if fyfy.arquivo:
                await userge.send_photo(
                    chat_id=chat.chat.id,
                    arquivo=fyfy.arquivo.file_id,
                    reply_to_message_id=message_id,
                )
            else:
                await userge.send_document(
                    chat_id=chat.chat.id,
                    document=fyfy.document.file_id,
                    reply_to_message_id=message_id,
                )
    except StopConversation:
        await message.err(
            "@spotipiebot Didn't respond in time\n:(  please try again later...", del_in=5
        )
