""" Módulo de testes para o @applled com fins de aprendizado """

from pyrogram.errors import BadRequest
from userge import Message, userge
from userge.utils import get_file_id


@userge.on_cmd(
    "neko",
    about={
        "info": "Obtenha a última versão do NekoX",
        "como usar": "neko nexox",
    },
)
async def app_neko(message: Message):
    """ Módulo para baixar a versão mais recente do NekoX """
    neko = message.input_str
    if not neko:
        await message.err("Apenas digite **Neko**.", del_in=10)
        return
    search = await message.edit("Procurando última atualização do: **{}**".format(neko))
    chat_id = message.chat.id
    f_id = ""
    try:
        async for msg in userge.search_messages(
            "NekoXAPKs", query=neko, limit=1, filter="document"
        ):
            f_id = get_file_id(msg)
    except BadRequest:
        await search.edit(
            "Obrigatório participar do deste [canal](https://t.me/NekoXAPKs)."
        )
        return
    if not f_id:
        await search.edit("Não encontrei por este termo... Tente de novo com <i>nekox</i>.", del_in=5)
        return
    await userge.send_document(chat_id, f_id)
    await search.delete()
