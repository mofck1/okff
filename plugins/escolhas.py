# @Laranjudo - Lindo e maravilhoso #
""" Módulo retrabalhado para o Modo Ausente com escolhas aleatórias"""
import asyncio
import random
from userge import Message, userge

# Motivos 
ASSISTINDO = (
        "𝚆𝚊𝚝𝚌𝚑𝚒𝚗𝚐, 𝙸'𝚕𝚕 𝚋𝚎 𝚋𝚊𝚌𝚔 𝚜𝚘𝚘𝚗.",
        "𝙹𝚞𝚜𝚝 𝚌𝚑𝚎𝚌𝚔 𝚖𝚢 @𝚝𝚠𝚊𝚙𝚙𝚕𝚎",
)
DORMINDO = (
        "𝙸 𝚓𝚞𝚜𝚝 𝚣𝚣𝚣...",
        "𝚣𝚣𝚣...",
        "𝙸'𝚖 𝚝𝚒𝚛𝚎𝚍, 𝚜𝚎𝚎 𝚢𝚊!",
)
OCUPADO = (
        "𝙱𝚄𝚂𝚈!",
        "𝙸 𝚌𝚊𝚗'𝚝 𝚝𝚊𝚕𝚔 𝚛𝚒𝚐𝚑𝚝 𝚗𝚘𝚠, 𝚜𝚘𝚛𝚛𝚢.",
        "𝚆𝚘𝚛𝚔𝚒𝚗𝚐 𝚘𝚗 𝚜𝚘𝚖𝚎𝚝𝚑𝚒𝚗𝚐.",
        "𝙽𝚊 𝚑𝚎𝚛𝚎...",
)
NETFLIX = (
        "𝙸'𝚖 𝚠𝚊𝚝𝚌𝚑𝚒𝚗𝚐 𝚘𝚗 𝙽𝚎𝚝𝚏𝚕𝚒𝚡.",
)

LOKI = (
#       "𝙷𝚎𝚕𝚕 𝚢𝚊, 𝚗𝚎𝚠 𝚎𝚙𝚒𝚜𝚘𝚍𝚎! 𝙱𝚢𝚎!",
        "𝙲𝚘𝚖𝚎 𝚘𝚗...",
)
#Temporário
SPOTIFY = (
        "𝙽𝚊 𝚑𝚎𝚛𝚎!\n𝙰 𝚐𝚘𝚘𝚍 𝙰𝚙𝚙𝚕𝚊𝚢𝚕𝚒𝚜𝚝 𝚒𝚜 𝚌𝚘𝚖𝚒𝚗𝚐 😊\n🎧 https://bit.ly/applefy ",
)
# Ações - Media dos Motivos 
ASSISTINDOM = (
        "https://telegra.ph/file/4fbbf7cd9953f017a0502.gif", #Criar novos layouts
        "https://telegra.ph/file/63d10879759183c8eac04.gif",
        "https://telegra.ph/file/19ef9c3c7f1fee430ec9d.gif",
)
#Add mais depois
DORMINDOM = (
        "https://telegra.ph/file/f59e0827bcb5c20011f7a.gif",
        "https://telegra.ph/file/4f9f9530d28c18f268b14.gif", 
        "https://telegra.ph/file/885d526a6d02910e436ef.gif",
        "https://telegra.ph/file/05baca30ed2ca52f0007f.gif",
        "https://telegra.ph/file/c2c84b023322fb234c206.gif",
)
OCUPADOM = (
        "https://telegra.ph/file/832926949334124fb23c9.gif",
        "https://telegra.ph/file/fe07e973e23fe725faab8.gif",
        "https://telegra.ph/file/6656a3c04a3626e862b7c.gif",
        "https://telegra.ph/file/140d286c155894093c250.gif",
        "https://telegra.ph/file/b2fda41d76cd798d4c368.gif",
        "https://telegra.ph/file/5eb616e8afe7a13fb401a.gif",
        "https://telegra.ph/file/c8689ace95f6a885066cd.gif",
        "https://telegra.ph/file/09211972875f5b340a8f3.gif,"
)
NETFLIXM = (
        "https://telegra.ph/file/d616384d44d96c7e912f7.gif",
)
#Temporário
LOKIM = (
        "https://telegra.ph/file/71b708eb44b9d2d3c60f6.gif",
#       "https://telegra.ph/file/b3236ef409f6d8bc69b1b.gif", 
#       "https://telegra.ph/file/c058c117801315f5af8f1.gif",
)
#Temporário
SPOTIFYM = (
        "https://telegra.ph/file/16abf23147a363828da13.gif",
)
@userge.on_cmd(
    "fui",
    about={
        "header": "Modo Ausente já definido os status/medias",
        "flags": {
            "-a": "Assistindo...",
            "-d": "Dormindo...",
            "-o": "Ocupado....",
            "-n": "Netflix...",
            "-l": "Loki...",
            "-s": "Spotify...",
        },
        "como usar": "{tr}fui -flag",
        "exemplo": "{tr}fui -a",
    },
    del_pre=True,
    allow_channels=False,
)

async def escolhas(message: Message):
    """ Motivos para o Modo Ausente """
    await message.edit("`𝙴𝚗𝚝𝚎𝚗𝚍𝚒, 𝙼𝚎𝚜𝚝𝚛𝚎. 𝙰𝚐𝚞𝚊𝚛𝚍𝚎... 𝙼𝚘𝚍𝚘 𝙰𝚞𝚜𝚎𝚗𝚝𝚎 𝚙𝚛é-𝚍𝚎𝚏𝚒𝚗𝚒𝚍𝚘 𝚊𝚝𝚒𝚟𝚊𝚍𝚘 ✅`", log=__name__)
    if "a" in message.flags:
            await message.edit(
                f"!afk {random.choice(ASSISTINDO)} | {random.choice(ASSISTINDOM)}",
                del_in=1,
            )
    if "d" in message.flags:
            await message.edit(
                f"!afk {random.choice(DORMINDO)} | {random.choice(DORMINDOM)}",
                del_in=1,
            )
    if "o" in message.flags:
            await message.edit(
                f"!afk {random.choice(OCUPADO)} | {random.choice(OCUPADOM)}",
                del_in=1
            )
    if "n" in message.flags:
            await message.edit(
                f"!afk {random.choice(NETFLIX)} | {random.choice(NETFLIXM)}",
                del_in=1
            )
    if "l" in message.flags:
            await message.edit(
                f"!afk {random.choice(LOKI)} | {random.choice(LOKIM)}",
                del_in=1
            )
    if "s" in message.flags:
            await message.edit(
                f"!afk {random.choice(SPOTIFY)} | {random.choice(SPOTIFYM)}",
                del_in=1
            )
