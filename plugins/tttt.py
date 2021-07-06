# Idea by @iTz_Black007

""" PEPEify via @honka_says_bot """

from userge import Message, userge
from userge.utils import deEmojify


@userge.on_cmd(
    "bla",
    about={
        "header": "Creates ",
        "flags": {"-m": "text ", "-l": "text "},
        "usage": "{tr}bla [text | reply to message]\n"
        "{tr}bla [flags] [text | reply to message]",
        "examples": ["{tr}blabla hehehe", "{tr}blabla [flags] Hehhe"],
    },
    allow_via_bot=False,
)
async def honka_says_bot(message: Message):
    """Creates"""
    replied = message.reply_to_message
    args = message.filtered_input_str
    if args:
        text = args
    elif replied:
        text = args or replied.text
    else:
        await message.err("Input not found!")
        return
    await message.delete()

    if "-l" in message.flags:
        font_size = 2
    elif "-m" in message.flags:
        font_size = 1
    else:
        font_size = 0

    try:
        stickers = await userge.get_inline_bot_results(
            "SpotifyNowBot", f"{deEmojify(text)}."
        )
        message_id = replied.message_id if replied else None
        await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=stickers.query_id,
            result_id=stickers.results[font_size].id,
            reply_to_message_id=message_id,
        )
    except IndexError:
        await message.err("List index out of range")
