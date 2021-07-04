""" Módulo de testes para o @applled com fins de aprendizado """

import gdshortener

from pyrogram.errors import YouBlockedUser
from userge import userge, Message
from userge.utils.exceptions import StopConversation


@userge.on_cmd("bitly", about={
    'header': "Encurte qualquer URL usando o bit.ly",
    'como usar': "{tr}bitly [link ou resposta]"}, allow_via_bot=False)
async def bitly(msg: Message):
    url = msg.input_or_reply_str
    if not url:
        await msg.err("Obrigatório uma URL aqui.")
        return
    try:
        async with userge.conversation("Sl_BitlyBot") as conv:
            await conv.send_message("/start")
            await conv.get_response(mark_read=True)
            await conv.send_message(url)
            shorten_url = (
                await conv.get_response(mark_read=True)
            ).text.split('\n', maxsplit=1)[-1]
            await msg.edit(f"Prontinho: {shorten_url}", disable_web_page_preview=True)
    except YouBlockedUser:
        await msg.edit("Desbloqueie o **@Sl_BitlyBot** para encurtar a URL")
    except StopConversation:
        await msg.err("O Bot está morto...")


@userge.on_cmd("isgd", about={
    'header': "Encurte qualquer URL usando o is.gd",
    'como usar': "{tr}isgd [link ou resposta]"})
async def is_gd(msg: Message):
    url = msg.input_or_reply_str
    if not url:
        await msg.err("Obrigatório uma URL aqui.")
        return
    s = gdshortener.ISGDShortener()
    try:
        s_url, stats = s.shorten(url, log_stat=True)
    except Exception as er:
        await msg.err(str(er))
    else:
        await msg.edit(
            f"**URL Encurtada:**\n`{s_url}`\n\n**Stats:** `{stats}`",
            disable_web_page_preview=True
        )


@userge.on_cmd("statsisgd", about={
    'header': "Reverta uma URL is.gd na original URl.",
    'como usar': "{tr}statsisgd [link ou resposta]"})
async def stats_is_gd(msg: Message):
    url = msg.input_or_reply_str
    if not url:
        await msg.err("Precisa de uma URL para verificar.")
        return
    s = gdshortener.ISGDShortener()
    try:
        original_url = s.lookup(url)
    except Exception as er:
        await msg.err(str(er))
    else:
        await msg.edit(
            f"**URL:** `{original_url}`",
            disable_web_page_preview=True
        )
