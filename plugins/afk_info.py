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
from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

LOGGER = userge.getLogger(__name__)

PLUS = (
    "𝐒𝐓𝐀𝐓𝐔𝐒 𝐏𝐄𝐑𝐒𝐎𝐍𝐀𝐋𝐈𝐙𝐀𝐃𝐎\n\n ╰• 𝙼𝚎𝚗𝚜𝚊𝚐𝚎𝚖 𝚊𝚙𝚊𝚐𝚊𝚍𝚊 𝚊𝚞𝚝𝚘𝚖𝚊𝚝𝚒𝚌𝚊𝚖𝚎𝚗𝚝𝚎 𝚎𝚖: 10seg\n\n𝐂𝐨𝐧𝐟𝐢𝐫𝐚 𝐬𝐞𝐮 𝐋𝐨𝐠 𝐂𝐡𝐚𝐧𝐧𝐞𝐥\n\n🔗 @twapple\n ╰• 𝚁𝚎𝚜𝚎𝚛𝚟𝚊𝚍𝚘 𝚙𝚊𝚛𝚊 𝚙𝚘𝚜𝚝𝚜 𝚊𝚕𝚎𝚊𝚝ó𝚛𝚒𝚘𝚜 𝚍𝚘 @𝚊𝚙𝚙𝚕𝚕𝚎𝚍",
)
CHEC = (
    "https://telegra.ph/file/b2fda41d76cd798d4c368.gif",
)

@userge.on_cmd(
    "afkplus",
    about={
        "header": "Módulo teste para o @applled",
    },
    del_pre=True,
    allow_channels=False,
    allow_via_bot=True,
)

async def inine_afk_status(msg):
    bot = await userge.bot.get_me()
    x = await userge.get_inline_bot_results(bot.username, "inline_info_afk")
    await msg.delete()
    await userge.send_inline_bot_result(
        chat_id=msg.chat.id, query_id=x.query_id, result_id=x.results[0].id 
    )
    return True

if userge.has_bot:

    @userge.bot.on_callback_query(filters.regex(pattern=r"^afk_extra"))
    async def runtime_info_(_, c_q: CallbackQuery):
        photo = f"""{random.choice(CHEC)}"""
        texto = f"{random.choice(PLUS)}"
                c_q.from_user.id
                await c_q.answer(
                "❌ Loading",
                show_alert=True,
            )
        
        buttons = [
            [
                InlineKeyboardButton('🏷 𝙴𝚗𝚟𝚒𝚊𝚛 𝙿𝙼', url='https://t.me/youcantbot'),
                InlineKeyboardButton('𝚂𝙴𝙲𝚁𝙴𝚃', callback_data="runtime_info"),
            ]
        ]
        try:
            await c_q.edit_message_media(
                media=InputMediaPhoto(media=photo, caption=texto),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except MessageNotModified:
            return
