from userge import Message, userge
from userge.utils import deEmojify
import random
from userge.plugins.utils.afk_inline import *


START = (
        "/start",
)
NOW = (
        "/now", 
)

@userge.on_cmd(
    "botfy",
    about={
        "header": "Teste do Apple",
        "uso": "{tr}botfy now[text | reply to message]\n"
        "{tr}botfy [flags] [text | reply to message]",
    },
    allow_via_bot=False,
)
async def SpotifyNowBot(message: Message):
    """Base teste @applled"""
    replied = message.reply_to_message
    now = message.input_str
    await send_inline_fy(message)
    )
    except IndexError:
        await message.err("@applled")
