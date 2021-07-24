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
    "fake",
    about={
        "titulo": "Teste",
        "descrição": "Teste",
        "como usar": "{tr}fake",
    },
)

async def foto_falsa(message: Message):
    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    if response.status_code == 200:
        with open("APPLEBOT.jpg", "wb") as f:
            f.write(response.content)
    resultado = f"Foto Fake Gerada\nFonte: ThisPersonDoesntExist.\nDivirta-se ;)"
    fake = "APPLEBOT.jpg"
    if message.reply_to_message:
        await client.send_photo(
            message.chat.id,
            photo=fake,
            caption=resultado,
            reply_to_message_id=message.reply_to_message.message_id,
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
