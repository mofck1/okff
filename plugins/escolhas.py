# @Laranjudo - Lindo e maravilhoso #
""" Módulo retrabalhado para o Modo Ausente com escolhas aleatórias"""
import asyncio
import random
from userge import Message, userge

# Motivos 
ASSISTINDO = (
        "Watching, I'll be back soon.",
        "Just check my @twapple",
)
DORMINDO = (
        "I just zzz...",
        "Zzz..",
        "I'm tired, see ya!",
)
OCUPADO = (
        "BUSY!",
        "I can't talk right now, sorry.",
        "Working on something.",
)
NETFLIX = (
        "__I'm watching on Netflix.__",
)

LOKI = (
        "__Hell ya, new episode! Bye!__",
        "__Come on...__",
)
# Ações - Media dos Motivos 
ASSISTINDOM = (
        "https://telegra.ph/file/4fbbf7cd9953f017a0502.gif", #Criar novos layouts
        "https://telegra.ph/file/63d10879759183c8eac04.gif",
        "https://telegra.ph/file/19ef9c3c7f1fee430ec9d.gif",
)
DORMINDOM = (
        "https://telegra.ph/file/4f9f9530d28c18f268b14.gif", #Add mais depois, estão repetidos
        "https://telegra.ph/file/318741f0d846727bdab7e.gif",
        "https://telegra.ph/file/885d526a6d02910e436ef.gif",
)
OCUPADOM = (
        "https://telegra.ph/file/832926949334124fb23c9.gif",
        "https://telegra.ph/file/fe07e973e23fe725faab8.gif",
        "https://telegra.ph/file/6656a3c04a3626e862b7c.gif",
        "https://telegra.ph/file/140d286c155894093c250.gif",
        "https://telegra.ph/file/b2fda41d76cd798d4c368.gif",
)
NETFLIXM = (
        "https://telegra.ph/file/d616384d44d96c7e912f7.gif",
)

LOKIM = (
        "https://telegra.ph/file/b3236ef409f6d8bc69b1b.gif", #Temporário
        "https://telegra.ph/file/c058c117801315f5af8f1.gif",
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
        },
        "como usar": "{tr}fui -flag",
        "exemplo": "{tr}fui -a",
    },
    del_pre=True,
    allow_channels=False,
)

async def escolhas(message: Message):
    """ Motivos para o Modo Ausente """
    await message.edit("`Entendi, Mestre. Aguarde...`", log=__name__)
#   LOG.info("Modo Ausente - Ativando..")
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
