
""" Manter os créditos | @applled - Música/Download """

import asyncio
import aiohttp
import requests

from pyrogram.errors import BadRequest
from userge import userge, Message


@userge.on_cmd(
    "amazon",
    about={
        "titulo": "Módulo criado pelo @applled - Amazon",
        "como usar": "{tr}amazon Redmi Note 8",
    },
    del_pre=True,
    allow_channels=False,
)
async def pesquisa_amazon(message: Message):
    query = message.input_str
    await message.edit("Pesquisando...")
    if not query:
        await message.edit("`Por favor, digite algo, né?`")
        return
    product = ""
    amazon_url = f"https://amznsearch.vercel.app/api/?query={query}"
    payload = {"format": "json", "url": amazon_url}
    r = requests.get("http://is.gd/create.php", params=payload)

        product = ""
        link = products['productLink']
        name = products['productName']
        price= products['productPrice']
        product += f"<a href='{link}'>• {name}\n{price}</a>\n"
    await message.edit(product, parse_mode="HTML")
