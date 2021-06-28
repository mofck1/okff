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
# Ações - Media dos Motivos 
ASSISTINDOM = (
        "https://telegra.ph/file/b66924aeae0d3485c28ac.mp4", #Criar novos layouts
        "https://telegra.ph/file/b66924aeae0d3485c28ac.mp4",
        "https://telegra.ph/file/b66924aeae0d3485c28ac.mp4",
)
DORMINDOM = (
        "https://telegra.ph/file/670badca8c8af12118f26.mp4", #Add mais depois, estão repetidos
        "https://telegra.ph/file/670badca8c8af12118f26.mp4",
        "https://telegra.ph/file/670badca8c8af12118f26.mp4",
)
OCUPADOM = (
        "https://telegra.ph/file/4fee33246f1b8dc90eb39.mp4",
        "https://telegra.ph/file/4fee33246f1b8dc90eb39.mp4",
        "https://telegra.ph/file/4fee33246f1b8dc90eb39.mp4",
)

@userge.on_cmd(
    "fui",
    about={
        "header": "Zoeira pra saber quais chances com a Purple",
        "flags": {
            "-a": "Ativa o afk com uma escolha aleatória já definida do motivo",
            "-d": "Dormindo.. ",
            "-o": "Ocupado... ",
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
