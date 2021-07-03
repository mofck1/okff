import os
import asyncio
from datetime import datetime
from PIL import Image
import asyncio
from userge import Config, Message, userge
from userge.utils import get_file_id, rand_array
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    User,
)

LOGGER = userge.getLogger(__name__)

@userge.on_cmd(
    "online",
    about={
        "header": "Módulo teste - @applled",
    },
    del_pre=True,
    allow_channels=False,
)

class Bot_Alive:
    @staticmethod
    async def check_media_link(media_link: str):
        match = _ALIVE_REGEX.search(media_link.strip())
        if not match:
            return None, None
        if match.group(1) == "i.imgur.com":
            link = match.group(0)
            link_type = "url_gif" if match.group(3) == "gif" else "url_image"
        elif match.group(1) == "telegra.ph/file":
            link = match.group(0)
            link_type = "url_image"
        else:
            link_type = "tg_media"
            if match.group(2) == "c":
                chat_id = int("-100" + str(match.group(3)))
                message_id = match.group(4)
            else:
                chat_id = match.group(2)
                message_id = match.group(3)
            link = [chat_id, int(message_id)]
        return link_type, link

async def apple(message: Message):
    await message.edit("**Checando...**\n**Aguarde, Mestre... **", log=__name__)
    photo = "https://telegra.ph/file/c8689ace95f6a885066cd.gif"
    texto = f"""
<a href="https://t.me/xapplebot"><b>APPLEBOT</a> IS ON AND UP ✓</b>
  <b><code>Online Since:{userge.uptime} | <b>Mode: {Bot_Alive._get_mode()}</code></b>
      ➖➖➖➖➖➖➖
 ⭕️   <b>Python:</b> <code>v{versions.__python_version__}</code>
 ⭕️   <b>Pyrogram:</b> <code>v{versions.__pyro_version__}</code>
 ⭕️   <b>Version:</b> <code>v1.0.Beta</code>
      ➖➖➖➖➖➖➖
 🍎   <b>Main:</b>  <b>@applled</b>

"""
    await userge.send_photo(message.chat.id, photo=photo, caption=texto,)
     try:
          await edit_message_text(
          Bot_Alive.alive_info(),
          reply_markup=Bot_Alive.alive_buttons(),
