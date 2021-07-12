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

@userge.on_cmd(
    "checking",
    about={
        "header": "Módulo teste para o @applled",
    },
    del_pre=True,
    allow_channels=False,
    allow_via_bot=True,
)

async def checking_teste(msg):
    if Config.ALLOW_NSFW.lower() == "true":
        return False
    bot = await userge.bot.get_me()
    x = await userge.get_inline_bot_results(bot.username, "checkin_info_")
    await msg.delete()
    await userge.send_inline_bot_result(
        chat_id=msg.chat.id, query_id=x.query_id, result_id=x.results[0].id
    )
    return True

if userge.has_bot:

    @userge.bot.on_callback_query(filters.regex(pattern=r"^runtime_info"))
    async def runtime_info(_, c_q: CallbackQuery):
        u_id = c_q.from_user.id
        if u_id not in Config.OWNER_ID and u_id not in Config.SUDO_USERS:
            return await c_q.answer(
                "Estou Online e Funcionando!",
                show_alert=True,
            )
        await c_q.answer("✅ Estou Online e Funcionando!", show_alert=False)
        msg = await userge.bot.get_messages("orugugu", 61)
        f_id = get_file_id(msg)
        buttons = [
            [
                InlineKeyboardButton(
                    text="Unsure / Change of Decision ❔",
                    callback_data="chg_of_decision_",
                )
            ]
        ]
        try:
            await c_q.edit_message_media(
                media=InputMediaPhoto(
                    media=f_id,
                    caption="Set <code>ALLOW_NSFW</code> = True in Heroku Vars to access this plugin",
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except MessageNotModified:
            pass

    @userge.bot.on_callback_query(filters.regex(pattern=r"^runtime_info"))
    async def age_verification_false(_, c_q: CallbackQuery):
        u_id = c_q.from_user.id
        if u_id not in Config.OWNER_ID and u_id not in Config.SUDO_USERS:
            return await c_q.answer(
                "Given That It's A Stupid-Ass Decision, I've Elected To Ignore It.",
                show_alert=True,
            )
        await c_q.answer("No I'm Not", show_alert=False)
        msg = await userge.bot.get_messages("orugu", 59)
        f_id = get_file_id(msg)
        img_text = "GO AWAY KID !"
        buttons = [
            [
                InlineKeyboardButton(
                    text="Unsure / Change of Decision ❔",
                    callback_data="chg_of_decision_",
                )
            ]
        ]
        try:
            await c_q.edit_message_media(
                media=InputMediaPhoto(media=f_id, caption=img_text),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except MessageNotModified:
            return

    @userge.bot.on_callback_query(filters.regex(pattern=r"^chg_of_decision_"))
    async def chg_of_decision_(_, c_q: CallbackQuery):
        u_id = c_q.from_user.id
        if u_id not in Config.OWNER_ID and u_id not in Config.SUDO_USERS:
            return await c_q.answer(
                "Given That It's A Stupid-Ass Decision, I've Elected To Ignore It.",
                show_alert=True,
            )
        await c_q.answer("Unsure", show_alert=False)
        msg = await userge.bot.get_messages("orugugu", 52)
        f_id = get_file_id(msg)
        img_text = "<b>ARE YOU OLD ENOUGH FOR THIS ?</b>"
        buttons = [
            [
                InlineKeyboardButton(
                    text="RUNTIME", callback_data="runtime_info"
                ),
                InlineKeyboardButton(
                    text="STATUS", callback_data="settings_btn"
                ),
            ]
        ]
        try:
            await c_q.edit_message_media(
                media=InputMediaPhoto(media=f_id, caption=img_text),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except MessageNotModified:
            pass
