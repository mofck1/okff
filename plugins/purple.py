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
    purple = (f"""
      **{(await userge.get_users(message.reply_to_message.from_user.id)).first_name}** 
      𝚂𝚞𝚊𝚜 𝚌𝚑𝚊𝚗𝚌𝚎𝚜 𝚌𝚘𝚖 𝚊 **Purple**
      ➖➖➖➖➖➖➖➖
      **🤡 Radar da Friendzone:** {random.choice(range(0,1000))}%
      **🥺 Chances de ganhar block:** {random.choice(range(0,10))} de 10
      **🌈 Te acha guei:** {random.choice(range(50,100))}%
      **💜 Suas chances são:** {random.choice(range(0,100))}% \nDe ser Verdade ou Mentira
      
      ➖➖➖➖➖➖➖➖
      Se não concordou, clique em /kickme
      🍏 PB - @applled | @twapple
      <code>Teste aprovado pela Anatel Astral</code>  
      """
)
        await message.client.send_animation(
                         message.chat.id, 
                         animation=purp, 
                         caption=purple,
        )
