""" Manter os créditos | @applled - Módulo que exibe qual música você está ouvindo no Spotify"""

from pyrogram.errors import BadRequest
from userge import userge, Message


@userge.on_cmd(
    "sig",
    about={
        "descrição": "Módulo criado pelo @applled - Resultado de um significado de uma palavra em Português.",
        "como usar": "{tr}sig maçã",
    },
    del_pre=True,
    allow_channels=False,
)
async def significado(message: Message):
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
        return await message.err("Lembre-se de fazer o comando + palavra", del_in=5)

    x = await userge.get_inline_bot_results(
            "@PriberamBot", input_query
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
        await message.err("Ops, talvez seja necessário dar /start no bot @PriberamBot", del_in=5)
