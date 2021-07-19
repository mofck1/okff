""" Teste do @applled """

from pyrogram.errors import BadRequest
from userge import Message, userge
from userge.utils import get_file_id


@userge.on_cmd(
    "gustavo",
    about={
        "titulo": "Teste",
        "como usar": ".gustavo /now",
    },
)
async def app_sistema(message: Message):
    """ Módulo teste """
    foto = message.input_str
    if not foto:
        await message.err("Use um comando do bot.", del_in=10)
        return
    search = await message.edit("𝙰𝚝𝚞𝚊𝚕𝚒𝚣𝚊𝚗𝚍𝚘... **{}**".format(foto))
    chat_id = message.chat.id
    f_id = ""
    try:
        async for msg in userge.search_messages(
            "spotipiebot", query=foto, limit=1, filter="photo"
        ):
            f_id = get_file_id(msg)
    except BadRequest:
        await search.edit(
            "Teste."
        )
        return
    if not f_id:
        await search.edit("**Falha na Matrix:** Não encontrei foi nada...", del_in=5)
        return
    await userge.send_photo(chat_id, f_id)
    await search.delete()
