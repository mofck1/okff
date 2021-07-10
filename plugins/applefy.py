""" Manter os créditos | @applled - Módulo que exibe qual música você está ouvindo no Spotify"""

from pyrogram.errors import BadRequest
from userge import userge, Message


@userge.on_cmd(
    "snow",
    about={
        "header": "Módulo criado pelo @applled que exibe qual música você está ouvindo no Spotify",
        "como usar": "{tr}snow /now",
    },
    del_pre=True,
    allow_channels=False,
)
async def appled_(message: Message):
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
        return await message.err("Lembre-se de fazer o comando + /now", del_in=5)

    x = await userge.get_inline_bot_results(
            "@spotipiebot", input_query
    )
    try:
        await message.delete()
        await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=x.query_id,
            result_id=x.results[0].id,
            reply_to_message_id=reply_id,
            hide_via=True
        )
    except (IndexError, BadRequest):
        await message.err("Pesquisa sem resultados...", del_in=5)


@userge.on_cmd(
    "now$",
    about={
        "header": "Módulo criado pelo @applled - Comando rápido para o Now Playing on Spotify",
         "flags": {
          "-n": "Now Playing",
          "-last": "NowP do LastFM",
        },
        "como usar": "{tr}now",
    },
    del_pre=True,
    allow_channels=False,
)
async def ouvindo_(message: Message):
    await message.edit("`✅`", del_in=1,)
    if "n" in message.flags:
            await message.edit(
                f"!snow /now",
                del_in=1,
            )
     if "last" in message.flags:
            await message.edit(
                f"!snow /last",
                del_in=1,
            )
