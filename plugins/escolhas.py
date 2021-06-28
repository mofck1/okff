# @Laranjudo - Lindo e maravilhoso #
""" Módulo retrabalhado para o Modo Ausente com escolhas aleatórias"""
import asyncio
import random
from userge import Message, userge

ASSISTINDO = (
        "APPLE",
        "ORANGE",
        "MANGO",
)
DORMINDO = (
        "APPLE",
        "ORANGE",
        "MANGO",
)
OCUPADO = (
        "APPLE",
        "ORANGE",
        "MANGO",
)

@userge.on_cmd(
    "escolhas",
    about={
        "header": "Zoeira pra saber quais chances com a Purple",
        "flags": {
            "-assistindo": "Ativa o afk com uma escolha aleatória já definida do motivo",
            "-dormindo": "--- ",
            "-ocupado": "--- ",
        },
        "como usar": "{tr}escolhas -flag",
        "exemplo": "{tr}escolhas -assistindo",
    },
    del_pre=True,
    allow_channels=False,
)

async def escolhas(message: Message):
    """ Motivos para o Modo Ausente """
    await message.edit("`Entendi, Mestre. Aguarde...`", log=__name__)
    LOG.info("Modo Ausente - Ativando..")
    if "assistindo" in message.flags:
            await message.edit(
                "`Teste`",
                del_in=3,
    if "dormindo" in message.flags:
            await message.edit(
                "`Teste`",
                del_in=3,
    if "ocupado" in message.flags:
            await message.edit(
                "`Teste`",
                del_in=3,
            )
