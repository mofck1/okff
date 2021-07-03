import os
import asyncio
from PIL import Image
import asyncio
from userge import Message, userge
from userge.utils import get_file_id, rand_array

MEDIA_ON = "https://telegra.ph/file/d50925c35883b16be6cd6.png"
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

async def apple(message: Message):
    await message.edit(
        f'**Checando...**\n**Aguarde, Mestre... **`')
    try:
    await userge.send_photo(online.chat_id,MEDIA_ON,caption=texto)
