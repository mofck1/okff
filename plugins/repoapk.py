""" Buscador de arquivos em APK - Teste do @applled """

from pyrogram.errors import BadRequest
from userge import Message, userge
from userge.utils import get_file_id


@userge.on_cmd(
    "apk",
    about={
        "titulo": "Pesquisa qualquer APK",
        "como usar": "apk Spotify",
    },
)
async def apkapplled(message: Message):
    """ Pesquise qualquer APK """
    aplicativo = message.input_str
    if not aplicativo:
        await message.err("Tente usar o nome de um app.", del_in=10)
        return
    search = await message.edit("Pesquisando por: **{}**".format(aplicativo))
    chat_id = message.chat.id
    f_id = ""
    try:
        async for msg in userge.search_messages(
            "Premium_droid", query=aplicativo, limit=1, filter="document"
        ):
            f_id = get_file_id(msg)
    except BadRequest:
        await search.edit(
            "Talvez você precise participar do deste [canal](https://t.me/Premium_droid)."
        )
        return
    if not f_id:
        await search.edit("Não encontrei foi nada...", del_in=5)
        return
    await userge.send_document(chat_id, f_id)
    await search.delete()
