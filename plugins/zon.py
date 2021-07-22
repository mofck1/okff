"""Pesquisa simplificada do Google - @applled"""

import requests

from userge import Message, userge


@userge.on_cmd(
    "zon",
    about={
        "titulo": "Módulo criado pelo @applled - Amazon",
        "como usar": "{tr}zon Redmi Note 8",
    },
    del_pre=True,
    allow_channels=False,
)
async def pesquisa_amazon(message: Message):
    """Amazon"""
    query = message.input_or_reply_str
    if not query:
        await message.edit("`Vou pesquisar o vento?!`")
        return
    query_encoded = query.replace(" ", "+")
    amazon_url = f"https://amznsearch.vercel.app/api/?query={query_encoded}"
    payload = {"format": "json", "url": amazon_url}
    r = requests.get("http://is.gd/create.php", params=payload)
    await message.edit(
        f"""
✅ **Este é o resultado da Sua Pesquisa:**
🔗 [{query}]({r.json()['shorturl']})

"""
    )
