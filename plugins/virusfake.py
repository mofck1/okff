## MÓDULO PARA ZOEIRA @applled(TG)

import asyncio
import os
import time
import random
from asyncio import sleep
from collections import deque
from random import choice, getrandbits, randint
from re import sub

import requests
import wget
from cowpy import cow

from userge import Message, userge

RICK = (
    "https://telegra.ph/file/74012d1cbe2a2d26e6a1a.gif",
)


@userge.on_cmd("virus$", about={"header": "Teste de plugin"})
async def laranja_func(message):
    user = await message.client.get_user_dict(message.from_user.id)
    heckerman = user["mention"]
    animation_chars = [
        "<code>Verificando o arquivo...</code>", 
        "<code>Executando análises...</code>", 
        "<code>Sim, sou rápido mesmo... </code>", 
        "<code>Ligando para o Tech Karan...</code>", 
        "<code>Kkk...</code>",
        "<code>LIGAÇÃO REJEITADA POR CONTER VÍRUS...</code>",
        "<code>Perdão pela mensagem anterior, estava em outro chat...</code>",
        "<code>Acessando catálogo de consultas...</code>",
        "<code>Ligando para todos os indianos...</code>", 
        "<code>Cruzando informações...</code>",
        "<code>Obtendo dados...</code>",
        "<code>Pronto... Aguarde o envio da resposta!</code>",
    ]
    funfou = (
        f"Tem vírus...\n <b>PODE INSTALAR TRANQUILO!</b>) "
    )
    max_ani = len(animation_chars)
    for i in range(max_ani):
        await asyncio.sleep(4)
        await message.edit(animation_chars[i % max_ani])
        photo = f"""{random.choice(RICK)}"""
        await message.client.send_animation(
                             caption=funfou,
                             animation=photo,
        )
