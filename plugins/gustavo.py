from pyrogram.errors import YouBlockedUser
from userge import Message, userge

@userge.on_cmd(
    "insta",
    about={
        "titulo": "Teste",
        "descrição": "Teste",
        "como usar": "{tr}insta + link",
    },
)
async def insta_download(message: Message):
    """Teste do @applled"""
    reply = message.reply_to_message
    insta = message.input_str
    if not insta:
        insta = message.input_str
    try:
    bot_ = "XTZ_InstagramBot"
    async with userge.conversation(bot_, timeout=1000) as conv:
        try:
            await conv.send_message(f"{insta}")
        except YouBlockedUser:
            await message.err("Dê /start em @XTZ_InstagramBot", del_in=5)
            return
        response = await conv.get_response(mark_read=True)
    erro = "Algo deu errado..."
    resp = response.text
    if erro in resp:
        await message.edit(
            f"Alguma coisa não deu certo aqui."
        )
    else:
        await message.edit(resp.html, parse_mode="html")
