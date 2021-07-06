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
async def _send_inline_fy(message: Message):
    now = message.input_str
    _bot = await userge.bot.get_me()
    fy = await userge.get_inline_bot_results("SpotifyNowBot", f"{deEmojify(now)}"
    await userge.send_inline_bot_result(
        chat_id=message.chat.id, query_id=_fy.query_id, result_id=_fy.results[0].id
    )
