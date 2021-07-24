import asyncio
from userge import Message, userge
from PIL import Image
import asyncio
import random
from userge import Config, Message, userge
from userge.utils import get_file_id, rand_array
from pyrogram import filters

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
  
