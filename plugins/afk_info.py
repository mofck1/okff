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
    if Config.ALLOW_NSFW.lower() == "true":
        return False
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
        u_id = c_q.from_user.id
        if u_id not in Config.OWNER_ID and u_id not in Config.SUDO_USERS:
#            return await c_q.answer(
#                "❌ Você não tem permissão para ver isto...",
#                show_alert=True,
#            )
        await c_q.answer("Extras", show_alert=True)
        msg = await userge.bot.get_messages("inlineApple", 6)
        f_id = get_file_id(msg)
        img_text = "𝐂𝐇𝐄𝐂𝐊 𝐓𝐇𝐈𝐒:\n\n𝐋𝐢𝐤𝐞 𝐓𝐰𝐞𝐞𝐭𝐬\n🔗 @twapple\n𝐁𝐢𝐨\n🔗 @orapple\n ╰• 𝘔𝘰𝘳𝘦 𝘤𝘰𝘮𝘪𝘯𝘨 𝘴𝘰𝘰𝘯..."
        buttons = [
            [
                InlineKeyboardButton('Enviar PM', url='https://t.me/youcantbot'),
            ]
        ]
        try:
            await c_q.edit_message_media(
                media=InputMediaPhoto(media=f_id, caption=img_text),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except MessageNotModified:
            return
