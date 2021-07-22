
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
    url = f"https://amznsearch.vercel.app/api/?query={query}"
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)
        r = await resp.json()
    if not r:
        return await message.edit("`Não consegui entrar nada ou estou quebrado. Morto?`")
    for products in r:
        link = products['productLink']
        name = products['productName']
        price= products['productPrice']
        product += f"<a href='{link}'>• {name}\n{price}</a>\n"
    await message.edit(product, parse_mode="HTML")
