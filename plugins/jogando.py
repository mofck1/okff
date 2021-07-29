""" Teste do @applled """

import asyncio
import os
import time
from asyncio import sleep
from collections import deque
from random import choice, getrandbits, randint
from re import sub

import requests
import wget
from cowpy import cow

from userge import Message, userge

@userge.on_cmd(
    "jogando",
    about={
        "titulo": "Status para Jogando algo no Telegram ;)",
        "jogos disponíveis": [
            "playing",
        ],
        "como usar": "{tr}jogando 400",
    },
)

async def jogando(message: Message):
    """Será que é verdade? Lol"""
    game = " GTA V"
    jogo = (
        "playing",
    )
    input_str = message.input_str
    args = input_str.split()
    if len(args) == 0:  #  
        jogando_tg = choice(jogo)
        tempo_jogo = randint(30, 60)
    elif len(args) == 1:  
        try:
            jogando_tg = str(args[0]).lower()
            tempo_jogo = randint(30, 60)
        except ValueError:
            jogando_tg = choice(jogo)
            tempo_jogo = int(args[0])
    elif len(args) == 2:  
        jogando_tg = str(args[0]).lower()
        tempo_jogo = int(args[1])
    else:
        await message.edit("`Infelizmente, não entendi e não sei se isto é possível.`")
        return
    try:
        if tempo_jogo > 0:
            chat_id = message.chat.id
            await message.delete()
            count = 0
            while count <= tempo_jogo:
                await message.client.send_chat_action(chat_id, jogando_tg, caption=game)
                await asyncio.sleep(5)
                count += 5
    except Exception:
        await message.delete()
