""" Módulo de testes para o @applled com fins de aprendizado  """

import random

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from userge import Message, userge

LOGGER = userge.getLogger(__name__)
CHECKS = (
    "https://telegra.ph/file/2b2799c01445dcc56a5bc.gif",
)


@userge.on_cmd(
    "on",
    about={
        "título": "Módulo teste para o @applled",
    },
    del_pre=True,
    allow_channels=False,
    allow_via_bot=False,
)
async def apple(message: Message):
    await userge.bot.get_me()
    master = await userge.get_me()
    await message.edit(
        "**Conectado...**\n𝙰𝚐𝚞𝚊𝚛𝚍𝚎 𝚘 𝚛𝚎𝚜𝚞𝚕𝚝𝚊𝚍𝚘, ;)", del_in=5, log=__name__
    )
    photo = f"""{random.choice(CHECKS)}"""
#   texto = f"<u>Estou Online</u>, {master.first_name}"
    await userge.bot.send_animation(
        message.chat.id,
        animation=photo,
#       caption=texto,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("+", callback_data="contato_pm"),
                    InlineKeyboardButton("TWAPPLE", url="https://t.me/twapple"),
                ]
            ]
        ),
    )
