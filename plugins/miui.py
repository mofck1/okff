""" Teste do @applled """

from pyrogram.errors import BadRequest
from userge import Message, userge
from userge.utils import get_file_id


@userge.on_cmd(
    "msu",
    about={
        "header": "Pesquisa um aplicativo direto do MIUI SYSTEM UPDATES",
        "usage": ".msu Clock",
    },
)
async def app_sistema(message: Message):
    """Teste, espero que funcione"""
    aplicativo = message.input_str
    if not aplicativo:
        await message.err("Tente usar o nome de um app.", del_in=10)
        return
    search = await message.edit("Pesquisando por: **{}**".format(document))
    chat_id = message.chat.id
    f_id = ""
    try:
        async for msg in userge.search_messages(
            -1203747311, query=document, limit=1, filter="document"
        ):
            f_id = get_file_id(msg)
    except BadRequest:
        await search.edit(
            "Obrigatório participar do deste [canal](https://t.me/MiuiSystemUpdates) "
        )
        return
    if not f_id:
        await search.edit("Não encontrei foi nada...", del_in=5)
        return
    await userge.send_document(chat_id, f_id)
    await search.delete()
