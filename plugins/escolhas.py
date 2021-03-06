# @Laranjudo - Lindo e maravilhoso #
""" MΓ³dulo retrabalhado para o Modo Ausente com escolhas aleatΓ³rias"""
import asyncio
import random
from userge import Message, userge

# Motivos 

PURPLE = (
    "Go away, I'm busy!",
)
AFK_REASONSS = (
    "Sorry, I'm busy right now. I'll be back later!",
)   
ANIMU = (
        "π°ππππ :3\nπ§ https://www.animu.com.br",
)
ASSISTINDO = (
        "ππππππππ, πΈ'ππ ππ ππππ ππππ.",
        "πΉπππ πππππ ππ’ @ππ πππππ",
)
DORMINDO = (
        "πΈ ππππ π£π£π£...",
        "π£π£π£...",
        "πΈ'π πππππ, πππ π’π!",
        "πΆπ ππ ππ’!",
)
OCUPADO = (
        "π±πππ!",
        "πΈ πππ'π ππππ πππππ πππ , πππππ’.",
        "πππππππ ππ πππππππππ.",
        "π½π ππππ...",
)
WORKING = (
        "πππππππ, πΈ πππ'π ππππ πππππ πππ .",
)

NETFLIX = (
        "πΈ'π π πππππππ ππ π½ππππππ‘.",
)
DISNEYPLUS = (
        "πΈ'π π πππππππ ππ Disney+.",
)

SPOTIFY = (
        "πΈ'π ππ πππππππ’ π\nπ§ https://bit.ly/applefy ",
)
# AΓ§Γ΅es - Media dos Motivos 
ASSISTINDOM = (
        "https://telegra.ph/file/4fbbf7cd9953f017a0502.gif", #Criar novos layouts
        "https://telegra.ph/file/63d10879759183c8eac04.gif",
        "https://telegra.ph/file/19ef9c3c7f1fee430ec9d.gif",
)
ANIMUM = (
        "https://telegra.ph/file/8c2fd1e064ee862a41ecf.gif",
        "https://telegra.ph/file/57fb5eb07d1e635a9a244.gif",
)

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
DISNEYPLUSM = (
        "https://telegra.ph/file/1d69b302fdb833f8c85ba.gif",
)
WORKINGM = (
        "https://telegra.ph/file/ef0fca4861e0b661e5fef.gif",
)
SPOTIFYM = (
        "https://telegra.ph/file/b26978b00e2ad40c67321.gif",
)
AFK_REASONSM = (
    "https://telegra.ph/file/5eb616e8afe7a13fb401a.gif"
) 
GIFF = (
    "https://telegra.ph/file/476963f68667b0e3d0fb3.gif",
    "https://telegra.ph/file/bb9f5906cfc9f0c5f16c7.gif",
)
PURP = (
    "https://telegra.ph/file/270775fff117922330729.gif",
)
@userge.on_cmd(
    "fui",
    about={
        "header": "Modo Ausente jΓ‘ definido os status/medias",
        "flags": {
            "-an": "Animu...",
            "-a": "Assistindo...",
            "-d": "Dormindo...",
            "-o": "Ocupado....",
            "-n": "Netflix...",
            "-s": "Spotify...",
            "-w": "Working...",
            "-p": "Working...",
            "-dd": "Disney+...",
        },
        "como usar": "{tr}fui -flag",
        "exemplo": "{tr}fui -a",
    },
    del_pre=True,
    allow_channels=False,
)

async def escolhas(message: Message):
    """ Motivos para o Modo Ausente """
    await message.edit("`π΄ππππππ, πΌπππππ. π°ππππππ... πΌπππ π°ππππππ ππΓ©-ππππππππ πππππππ β`", log=__name__)
    if "a" in message.flags:
            await message.edit(
                f"!afk {random.choice(ASSISTINDO)} | {random.choice(ASSISTINDOM)}",
                del_in=1,
            )
    if "an" in message.flags:
            await message.edit(
                f"!afk {random.choice(ANIMU)} | {random.choice(ANIMUM)}",
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
    if "s" in message.flags:
            await message.edit(
                f"!afk {random.choice(SPOTIFY)} | {random.choice(SPOTIFYM)}",
                del_in=1
            )
    if "w" in message.flags:
            await message.edit(
                f"!afk {random.choice(WORKING)} | {random.choice(WORKINGM)}",
                del_in=1
            )
    if "p" in message.flags:
            await message.edit(
                f"!afk {random.choice(PURPLE)} | {random.choice(PURP)}",
                del_in=1
            )
    if "dd" in message.flags:
            await message.edit(
                f"!afk {random.choice(DISNEYPLUS)} | {random.choice(DISNEYPLUSM)}",
                del_in=1
            )

@userge.on_cmd(
    "bye",
    about={
        "titulo": "Gone!",
        "como usar": "{tr}bye",
        "exemplo": "{tr}bye",
    },
    del_pre=True,
    allow_channels=False,
)

async def gone(message: Message):
    gif = f"""{random.choice(GIFF)}"""
    mensagem = f"<i>I'v to go, bye!</i> :3"
    await message.client.send_animation(
                         message.chat.id, 
                         animation=gif, 
                         caption=mensagem,
    )    
