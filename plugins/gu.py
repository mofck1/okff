
from pyrogram.errors import YouBlockedUser
from userge import Message, userge


@userge.on_cmd(
    "gu",
    about={
        "titulo": "teste",
        "descrição": "só um teste mesmo",
        "como usar": "{tr}gu link",
    },
)
async def gu_teste(message: Message):
    """vamos lá, tira a cadeira do sofá"""
    reply = message.reply_to_message
    bot_ = "XTZ_InstagramBot"
    async with userge.conversation(bot_, timeout=1000) as conv:
        try:
            await conv.send_message(f"{reply}")
        except YouBlockedUser:
            await message.err("Dê /start no @XTZ_InstagramBot", del_in=5)
            return
        response = await conv.get_response(mark_read=True)
    fail = "Algo deu errado..."
    resp = response.text
    if fail in resp:
        await message.edit(
            f"Joga fora no lixo."
        )
    else:
        await message.edit(resp.html, parse_mode="html")
