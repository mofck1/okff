import asyncio
from userge import Message, userge
from PIL import Image
import asyncio
import random
from userge import Config, Message, userge
from random import choice, getrandbits, randint
from userge.utils import get_file_id, rand_array
from pyrogram import filters

RESULTADO = (
    "https://boredhumans.b-cdn.net/faces2/",
)

@userge.on_cmd(
    "fake",
    about={
        "titulo": "Teste",
        "descrição": "Teste",
        "como usar": "{tr}fake",
    },
)
async def falso_teste(message: Message):
    await message.edit(f"Carregando...", del_in=5, log=__name__)
    falso = f"""{random.choice(RESULTADO)}{random.choice(range(0,994))}.jpg"""
    texto = f"**Foto Fake Gerada** ✅\n**Fonte:** <i>BoredHumans.</i>\n\nDivirta-se ;)"
    await message.client.send_photo(
                         message.chat.id, 
                         photo=falso, 
                         caption=texto,
    )
    
async def verifica_envia(message: Message, *args, **kwargs):
    replied = message.reply_to_message
    if replied:
        await asyncio.gather(message.delete(), replied.reply(*args, **kwargs))
    else:
        await message.edit(*args, **kwargs)
