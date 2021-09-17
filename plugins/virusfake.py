""" Módulo de testes para o @applled(TG) com fins de aprendizado """

import os
import asyncio
from datetime import datetime
from PIL import Image
import asyncio
import random
from userge import Config, Message, userge
from userge.utils import get_file_id, rand_array
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

LOGGER = userge.getLogger(__name__)

RICK = (
    "https://telegra.ph/file/74012d1cbe2a2d26e6a1a.gif",
)

MENSAGEM = (
    "Tem vírus...\n<b>PODE INSTALAR TRANQUILO!</b>",
)

@userge.on_cmd("virus$", about={"header": "Teste de plugin"})
async def laranja_func(message):
    photo = f"""{random.choice(RICK)}"""
    texto = f"""{random.choice(MENSAGEM)}"""
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

    
    max_ani = len(animation_chars)
    for i in range(max_ani):
        await asyncio.sleep(3)
        await message.edit(animation_chars[i % max_ani], del_in=1)
        await message.client.send_animation(
                             message.chat.id, 
                             caption=funfou,
                             animation=photo,
        )
