from userge import Message, userge
from userge.utils import deEmojify
import random

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
    fy = await userge.get_inline_bot_results("SpotifyNowBot", f"{deEmojify(now)}"
        )
        message_id = replied.message_id if replied else None
        await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            result_id=fy.results[now].id,
            reply_to_message_id=message_id,
        )
    except IndexError:
        await message.err("@applled")
