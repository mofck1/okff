import os
import asyncio
from PIL import Image
import asyncio
from userge import Message, userge
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

    @userge.bot.on_callback_query(filters.regex(pattern=r"^teste_apple$"))
    async def _teste_apple(_, c_q: CallbackQuery):
        c_q.from_user.id
        await c_q.answer(
            f"𝐀𝐩𝐩𝐥𝐞𝐁𝐨𝐭 𝐓𝐞𝐚𝐦:\n𝚆𝚘𝚛𝚔𝚒𝚗𝚐 𝚘𝚗 𝙱𝚘𝚝\n\n o/",
            show_alert=True,
        )
        return _teste_apple

async def apple(message: Message):
    await message.edit("'**Checando...**\n**Aguarde, Mestre... **`'", log=__name__)
    photo = "https://telegra.ph/file/c8689ace95f6a885066cd.gif"
    texto = "**APPLEBOT** is **UP AND RUN**\n\nMain: @applled"
    await userge.send_photo(message.chat.id, photo=photo, caption=texto, reply_markup=InlineKeyboardMarkup(buttons))
    buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("TESTE", url=Config.MEUTG_REPO)],
                [InlineKeyboardButton("TESTE 2", callback_data="teste_apple")],
            ]
        )
    del_in=20,
