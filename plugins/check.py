import os
import asyncio
from datetime import datetime
from PIL import Image
import asyncio
import random
from userge import Config, Message, userge
from userge.utils import get_file_id, rand_array
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

LOGGER = userge.getLogger(__name__)
    
@userge.on_cmd(
    "check",
    about={
        "header": "Módulo teste - @applled",
    },
    del_pre=True,
    allow_channels=False,
)
class Check_Info:
async def apple(message: Message):
    await message.edit("**Iniciando checagem...**\nAguarde o resultado, Mestre...", log=__name__)
#   photo = "{random.choice(CHECKS)}"
    texto = "__I'm Online, @appled!__"
    await message.client.send_animation(
                         message.chat.id, 
                         animation=Check_Info.media_check_(), 
                         caption=texto)

    def media_check_() -> str:
        m_imgs = [
    "https://telegra.ph/file/b2fda41d76cd798d4c368.gif",
    "https://telegra.ph/file/43901682e8a936d76572e.gif",
    "https://telegra.ph/file/140d286c155894093c250.gif",
    "https://telegra.ph/file/ebfb744d7a25736ef09f5.gif",
        ]
        return rand_array(m_imgs)
                
   #Adicionar outras configurações
