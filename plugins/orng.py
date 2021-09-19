import textwrap
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from requests import get


@userge.on_cmd(
    "teste",
    about={
        "titulo": "teste",
        "descrição": "O próprio título já explica",
        "como usar": "{tr}teste",
    },
)

async def testei_imagem(u_name: str):
    """nada demais"""
    text1 = "@applled " + u_name
    text2 = f"Teste de texto aqui {u_name} mais texto e mais texto do Orange."
    in_memory = BytesIO(
        get("https://telegra.ph/file/6cfa492e416552db189e8.jpg").content
    )
    photo = Image.open(in_memory)
    drawing = ImageDraw.Draw(photo)
    white = (255, 255, 255)
    font1 = ImageFont.truetype("resources/Roboto-Regular.ttf", 45)
    font2 = ImageFont.truetype("resources/Roboto-Medium.ttf", 55)
    drawing.text((132, 201), text1, fill=white, font=font2)
    x = 0
    for u_text in textwrap.wrap(text2, width=38):
        drawing.text(xy=(132, 305 + x), text=u_text, font=font1, fill=white)
        x += 53
    new_pic = BytesIO()
    photo.save(new_pic, format="JPEG")
    new_pic.name = "Apple.jpg"
    return new_pic
