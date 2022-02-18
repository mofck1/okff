""" Manter os créditos | """

import random

from pyrogram.errors import BadRequest

from userge import Message, userge

NOW = ("latest",)
COMANDO = ("of",)


@userge.on_cmd(
    "geek",
    about={
        "header": "teste",
        "como usar": "{tr}geek /of",
    },
    del_pre=True,
    allow_channels=False,
)
async def geek_(message: Message):
    reply = message.reply_to_message
    reply_id = reply.message_id if reply else None
    if message.input_str:
        input_query = message.input_str
    elif reply:
        if reply.text:
            input_query = reply.text
        elif reply.caption:
            input_query = reply.caption
    if not input_query:
        return await message.err("Lembre-se de fazer o comando", del_in=5)

    x = await userge.get_inline_bot_results("@XiaomiGeeksBot", input_query)
    try:
        await message.delete()
        await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=x.query_id,
            result_id=x.results[0].id,
            reply_to_message_id=reply_id,
            hide_via=True,
        )
    except (IndexError, BadRequest):
        await message.err(
            "Erro.",
            del_in=5,
        )
        
        @userge.on_cmd(
    "gk$",
    about={
        "título": "tttt."
    },
    trigger="",
    allow_via_bot=False,
)
async def ouvindo_(message: Message):
    await message.edit(
        "!of /of",
        del_in=1,
    )
