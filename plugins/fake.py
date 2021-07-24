import asyncio
from userge import Message, userge
from PIL import Image
import asyncio
import random
from userge import Config, Message, userge
from userge.utils import get_file_id, rand_array
from pyrogram import filters

RESULTADO = (
    "https://thispersondoesnotexist.com/image",
)

@userge.on_cmd(
    "fake2",
    about={
        "titulo": "Teste",
        "descrição": "Teste",
        "como usar": "{tr}fake2",
    },
)
async def falso_teste(message: Message):
    await message.edit(f"Aguarde...", del_in=5, log=__name__)
    photo = f"""{random.choice(RESULTADO)}"""
    texto = f"Foto Fake Gerada\nFonte: ThisPersonDoesntExist.\nDivirta-se ;)"
    await message.client.send_animation(
                         message.chat.id, 
                         animation=photo, 
                         caption=texto,
    )
