""" Módulo de testes para o @applled com fins de aprendizado """

import os
import asyncio
import requests
import json
from userge import Config, Message, userge
from userge.utils import get_file_id, rand_array

@userge.on_cmd(
    "url",
    about={
        "header": "Módulo teste para o @applled",
    },
    del_pre=True,
    allow_channels=False,
)
 
async def encurtador(message: Message):
    if message.forward_message:
        return
    input_str = message.pattern_match.group(1)
    encurta_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(encurta_url).text
    if response_api:
        await userge.client.forward_messages("Gerando {} para {}.".format(response_api, input_str))
    else:
        await message.edit("Algo não está certo, tente de novo.")
