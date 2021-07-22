from pyrogram.errors import BadRequest
from userge import userge, Message
import requests

@userge.on_cmd(
    "teste",
    about={
        "titulo": "Módulo criado pelo @applled - teste",
        "como usar": "{tr}teste",
    },
    del_pre=True,
    allow_channels=False,
)

async def teste_(message: Message):
    engine = message.Engine
    apple = await edit_or_reply(message, engine.get_string("PROCESSANDO"))
    laranja = get_text(message)
    if not laranja:
        await apple.edit(
            engine.get_string("OBRIGATÓRIO TEXTO").format("Text")
        )
        return
    orange = laranja.split(":")
    search = orange[0]
    try:
        result = orange[1]
    except:
        await apple.edit(
            engine.get_string("OBRIGATÓRIO TEXTO").format("Text")
        )
        return
    photo = f"https://telegra.ph/file/376c89b2ef6c6ddbb2fe4.jpg"
    drawing = ImageDraw.Draw(photo)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font1 = ImageFont.truetype("./fontes/ProductSans-BoldItalic.ttf", 20)
    font2 = ImageFont.truetype("./fontes/ProductSans-Light.ttf", 23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    file_name = "teste.jpg"
    photo.save(file_name)
    await pablo.delete()
    if message.reply_to_message:
        await client.send_photo(
            message.chat.id,
            photo=file_name,
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await client.send_photo(message.chat.id, photo=file_name)
    if os.path.exists(file_name):
        os.remove(file_name)
