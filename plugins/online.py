import asyncio
from userge import Message, userge
from userge.utils import get_file_id, rand_array

MEDIA_ON = "https://telegra.ph/file/fc3aef09eb9b82d244f97.jpg"
texto = "**APPLEBOT** is **UP AND RUN**\n\n"
texto += "Main: @applled"

LOGGER = userge.getLogger(__name__)

@userge.on_cmd(
    "online",
    about={
        "header": "Módulo teste - @applled",
    },
    del_pre=True,
    allow_channels=False,
)

async def apple(online):
    chat = await online.get_chat()
    """ Teste de módulo """
    await userge.send_file(online.chat_id,MEDIA_ON,caption=texto)
