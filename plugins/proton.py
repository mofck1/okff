""" @Applled - Lindo e maravilhoso """

import asyncio
import random
from userge import Message, userge

@userge.on_cmd("pro$", about={"título": "Tu sabe o que é :D"}, trigger="", allow_via_bot=False)
async def proton_msg(message: Message):
    await message.edit(
        "**-.-. --- -- . -. - .-. .. --- / .--. .-. . -- .. ..- --", del_in=2, log=__name__
    )
    texto = f"ⓘ <i>Essa mensagem está disponível apenas para usuários da ProtonAOSP Premium.</i> <u>[Saiba mais](https://bit.ly/protonpremium)</u>"
    await message.edit(
        message.chat.id,
        caption=texto,
        disable_web_page_preview=True,
    )
