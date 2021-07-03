import os
import asyncio
from PIL import Image
import asyncio
from userge import Message, userge
from userge.utils import get_file_id, rand_array


LOGGER = userge.getLogger(__name__)

@userge.on_cmd(
    "online",
    about={
        "header": "Módulo teste - @applled",
    },
    del_pre=True,
    allow_channels=False,
)

async def apple(message: Message):
    await message.edit("'**Checando...**\n**Aguarde, Mestre... **`'", log=__name__)
    photo = "https://telegra.ph/file/d50925c35883b16be6cd6.png"
    texto = "**APPLEBOT** is **UP AND RUN**\n\nMain: @applled"
    await userge.send_photo(message.chat.id, photo=photo, caption=texto)
    del_in=20,
