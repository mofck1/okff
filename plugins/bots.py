""" Verifica quantos bots existem em um grupo - Ideia do Ash adaptado pelo Orange """

from userge import Message, userge
from PIL import Image
import asyncio
import random
from userge import Config, Message, userge
from userge.utils import get_file_id, rand_array
from pyrogram import filters

BOTS = (
    "https://telegra.ph/file/ac5bbccca2eee5f109c8a.gif",
    "https://telegra.ph/file/ac5bbccca2eee5f109c8a.gif",
)

@userge.on_cmd(
    "bots",
    about={
        "titulo": "Verifica quantos bots existem no grupo",
        "descrição": "O próprio título já explica",
        "como usar": "{tr}bots",
    },
)
async def verifica_bot(message: Message):
    """ Verifica quantos bots existem no grupo """
    await message.edit("**Coletando dados...**\n𝙰𝚐𝚞𝚊𝚛𝚍𝚎...", del_in=5,)
    photo = f"""{random.choice(BOTS)}"""
    chat = message.chat.id
    admin_b = []
    member_b = []
    total = 0
    async for bot in userge.iter_chat_members(chat, filter="bots"):
        total += 1
        mention = bot.user.mention
        if bot.status == "administrator":
            admin_b.append(mention)
        else:
            member_b.append(mention)
    adm = len(admin_b)
    mem = len(member_b)
    out = f"🏷 <b>BOTS NESTE GRUPO</b>\n ({message.chat.title})\n"
    out += f" ╰•    [{total}]\n\n"
    out += f"<b>ADMINISTRADORES</b>\n"
    out += f" ╰•    [{adm}]\n\n"
    out += f"<b>LISTA DE BOTS:</b>\n"
    out += f" ╰•    [{mem}]\n\n"
    out += "\n▫️".join(admin_b)
    out += "\n\n" if admin_b else "\n"
    out += "▫️" if member_b else ""
    out += "\n▫️".join(member_b)
    await message.client.send_animation(
                         animation=photo, 
                         caption=out,
    )
    
    # Alterar o Out para teste depois #
