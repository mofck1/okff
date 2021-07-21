""" @Applled """

import os
import re

import asyncio
import random
import requests
import lyricsgenius
from bs4 import BeautifulSoup
from googlesearch import search
from userge import Message, userge
from random import choice, getrandbits, randint
from userge.utils import get_file_id, rand_array

MEDIA = (
    "https://telegra.ph/file/b26978b00e2ad40c67321.gif",
)

@userge.on_cmd(
    "letra",
    about={
        "titulo": "Letras fornecidas pelo Genius Lyrics",
        "Info": "letras de vindo do Genius.com",
        "Como usar": "{tr}letras [nome da música]",
        "exemplo": "{tr}letras What is love Haddaway",
    },
)
async def glyrics(message: Message):
    letra = f"""{random.choice(MEDIA)}"""
    song = message.input_str
    if not song:
        await message.edit("Bugadão kkk")
        return
    await message.edit(f"__Pesquisando por {song}__")
    to_search = song + "genius lyrics"
    gen_surl = list(search(to_search, num=1, stop=1))[0]
    gen_page = requests.get(gen_surl)
    scp = BeautifulSoup(gen_page.text, "html.parser")
    lyrics = scp.find("div", class_="lyrics")
    if not lyrics:
        await message.edit(f"Não consegui encontrar: `{song}`")
        return
    lyrics = lyrics.get_text()
    lyrics = re.sub(r"[\(\[].*?[\)\]]", "", lyrics)
    lyrics = os.linesep.join((s for s in lyrics.splitlines() if s))
    title = scp.find("title").get_text().split("|")
    writers_box = [
        writer
        for writer in scp.find_all("span", {"class": "metadata_unit-label"})
        if writer.text == "Escrita por"
    ]
    if writers_box:
        target_node = writers_box[0].find_next_sibling(
            "span", {"class": "metadata_unit-info"}
        )
        writers = target_node.text.strip()
    else:
        writers = "Desconhecido"
    lyr_format = ""
    lyr_format += "**" + title[0] + "**\n"
    lyr_format += "__" + lyrics + "__"
    lyr_format += "\n\n**Escrita por: **" + "__" + writers + "__"
    lyr_format += "\n**Fonte: **" + "`" + title[1] + "`"

        await message.client.send_animation(
                         message.chat.id, 
                         animation=letra, 
                         caption=lyr_format,
        )
