""" Módulo criado pelo @applled - Inspirado na maravilhosa Purple <3 | Manter os créditos para @applled """

import asyncio
import random
import time
from asyncio import sleep
from random import choice, getrandbits, randint

import requests
from userge import Message, userge
from userge.utils import get_file_id, rand_array

CARREGADO = (
    "https://telegra.ph/file/d4eaad9d72a0c1f5fb676.gif",
)

@userge.on_cmd("purple$", about={"header": "Quais as suas chances com a Purple?"})
async def purple_func(message):
    user = await message.client.get_user_dict(message.from_user.id)
    purp = f"""{random.choice(CARREGADO)}"""
    gerando = [
        "▫️ Iniciando o teste...", 
        "▫️ Consultando o horóscopo...",
        "▫️ Invocando o Zodíaco... ",
        "▫️ E os Cavaleiros, claro... ",
        "▫️ Conversando com a Purple..."
        "▫️ Atena Liberou ✅", 
        "▫️ Anatel Aprovou ✅",
        "····",
        "·····",
        "····",
        "······",
        "········",        
        "▫️ Gerando o resultado...",      
    ]
    
    purple = (f"""
      **{(await userge.get_users(message.reply_to_message.from_user.id)).first_name}** - Suas chances com a **Purple**
      ➖➖➖➖➖➖➖➖
      **🤡 Radar da Friendzone :** {random.choice(range(0,1000))}%
      **🥺 Chances de ganhar block :** {random.choice(range(0,10))} de 10
      **🤏🏻 Te acha guei :** {random.choice(range(50,100))}%
      **💜 Suas chances são :** {random.choice(range(0,100))}% de ser verdade/mentira
      ➖➖➖➖➖➖➖➖
      Se não concordou, clique em /kickme
      🍏 PB - @applled | @twapple
      <code>Teste aprovado pela Anatel Astral</code>  
      """
)
    max_ani = len(gerando)
    for i in range(max_ani):
        await asyncio.sleep(1)
        await message.edit(gerando[i % max_ani])
        await message.client.send_animation(
                         message.chat.id, 
                         animation=purp, 
                         caption=purple,
        )
    
