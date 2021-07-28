""" Isso é só um teste, pelo amor.. """

from userge import userge, Message, Config
from pyrogram import (  
     InlineKeyboardMarkup, 
     InlineKeyboardButton, 
     Filters, 
     CallbackQuery
)

if Config.BOT_TOKEN and Config.OWNER_ID:
    if Config.HU_STRING_SESSION:
        ubot = userge.bot
    else:
        ubot = userge
 

    def dono_filter() -> filters:
        async def func(_, __, m: Message) -> bool:
            text = m.text or m.caption
            bot_ = (await get_bot_info()).get("bot")
            username = "@" + bot_.uname if bot_ else ""
            pattern = comp_regex(f"(?i)^/dono({username})?([\s]+)?$")
            m.matches = (list(pattern.finditer(text)) if text else None) or None
            return bool(
                (m.chat and m.chat.type == "private") and m.matches and not m.edit_date
            )

        return filters.create(func, "DonoFilter")
      
    @userge.bot.on_message(dono_filter())    
    async def dono_bot(_, message: Message):
        bot = await userge.bot.get_me()
        master = await userge.get_me()
        mensagem = f"""Olá, sou o \"{bot.username}\" - Assistente Pessoal do {master.first_name}. 
        Vida que segue. ;)\n\n"""
        mensagem += f"Links úteis:\nGoogle.com\nHeroku.com\m"
        await message.reply(
                mensagem,
                disable_web_page_preview=True,
                parse_mode="markdown",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        "Twapple",
                        url=f"t.me/twapple"
                    ),
                    InlineKeyboardButton(
                        "AppleBot",
                        switch_inline_query=""
                    )
                ]])
            )
