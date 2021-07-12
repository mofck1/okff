""" Módulo de testes para o @applled com fins de aprendizado  """

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
CHECKS = (
    "https://telegra.ph/file/b2fda41d76cd798d4c368.gif",
    "https://telegra.ph/file/43901682e8a936d76572e.gif",
    "https://telegra.ph/file/140d286c155894093c250.gif",
    "https://telegra.ph/file/ebfb744d7a25736ef09f5.gif", 
)

@userge.on_cmd(
    "check",
    about={
        "header": "Módulo teste para o @applled",
    },
    del_pre=True,
    allow_channels=False,
    allow_via_bot=True,
)

async def apple(message: Message):
    await message.edit("**𝚃𝚎𝚜𝚝𝚎 𝚐𝚎𝚛𝚊𝚍𝚘...**\n𝙰𝚐𝚞𝚊𝚛𝚍𝚎 𝚘 𝚛𝚎𝚜𝚞𝚕𝚝𝚊𝚍𝚘, 𝙼𝚎𝚜𝚝𝚛𝚎...", del_in=5, log=__name__)
    photo = f"""{random.choice(CHECKS)}"""
    texto = "<u>Estou Online</u>, @applled!"
    await message.client.send_animation(
                         message.chat.id, 
                         animation=photo, 
                         caption=texto,
                         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝙽𝙾𝚃Í𝙲𝙸𝙰𝚂', callback_data="teste_apple"),
                    InlineKeyboardButton('𝚃𝚆𝙰𝙿𝙿𝙻𝙴', url='https://t.me/twapple'),
                ]
            ]
        )
    )

            @userge.bot.on_callback_query(filters.regex(pattern=r"^teste_apple$"))
    async def age_verification_true(_, c_q: CallbackQuery):
        u_id = c_q.from_user.id
        if u_id not in Config.OWNER_ID and u_id not in Config.SUDO_USERS:
            return await c_q.answer(
                "Ok, testado.",
                show_alert=True,
            )
        await c_q.answer("Continuar", show_alert=False)
        msg = await userge.bot.get_messages("orugugu", 61)
        f_id = get_file_id(msg)
        buttons = [
            [
                InlineKeyboardButton(
                    text="Voltar",
                    callback_data="teste_apple",
                )
            ]
        ]
        try:
            await c_q.edit_message_media(
                media=InputMediaPhoto(
                    media=f_id,
                    caption="Pois é...",
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except MessageNotModified:
            pass
