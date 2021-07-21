""" Verifica quantos bots existem em um grupo - Ideia do Ash refeito pelo Orange """

import asyncio
from userge import Message, userge
from PIL import Image
import asyncio
import random
from userge import Config, Message, userge
from userge.utils import get_file_id, rand_array
from pyrogram import filters

BOTS = (
    "https://telegra.ph/file/6a40587cbf58e1a77eccf.gif",
    "https://telegra.ph/file/370cad02110707898bdc4.gif",
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
    out = f"🏷 𝚁𝙴𝚂𝚄𝙻𝚃𝙰𝙳𝙾 𝙳𝙰 𝚂𝚄𝙰 𝙿𝙴𝚂𝚀𝚄𝙸𝚂𝙰\n𝙽𝚎𝚜𝚝𝚎 𝙶𝚛𝚞𝚙𝚘 | ({message.chat.title})\n"
    out += f" ╰•  [{total}] <i>Bot(s)</i>\n\n"
    out += f"𝙰𝙳𝙼𝙸𝙽𝙸𝚂𝚃𝚁𝙰𝙳𝙾𝚁𝙴𝚂: [{adm}]\n"
    out += f"𝙲𝙾𝙼𝚄𝙽𝚂: [{mem}]\n<i>Bots sem privilégios administrativos.</i>\n"
    out += "\n".join(admin_b)
    out += "\n\n" if admin_b else "\n"
    out += "▫️" if member_b else ""
    out += "\n".join(member_b)
    await message.client.send_animation(
                         message.chat.id, 
                         animation=photo, 
                         caption=out,
    )
