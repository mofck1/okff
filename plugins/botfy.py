from userge import Message, userge
from userge.utils import deEmojify

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
    args = message.filtered_input_str
    if args:
        text = args
    elif replied:
        text = args or replied.text
    else:
        await message.err("Vento")
        return
    await message.delete()

    if "start" in message.flags:
            await message.edit(
                f"!botfy {random.choice(START)}",
                del_in=3,
            )
    if "now" in message.flags:
            await message.edit(
                f"!afk {random.choice(NOW)}",
                del_in=3,
            )

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
        await message.err("@applled")
