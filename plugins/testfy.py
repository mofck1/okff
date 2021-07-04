from userge import Message, userge
from userge.utils import deEmojify


@userge.on_cmd(
    "fyfy",
    about={
        "header": "TESTE",
        "flags": {"-n": "teste"},
        "uso": "{tr}fyfy"
    },
    allow_via_bot=False,
)
async def SpotifyNowBot(message: Message):
    """ Applled """
    spotify = "/start"
    now = "/now"
    async with userge.conversation("SpotifyNowBot") as conv:
        await conv.send_message("/start")
        await conv.send_message("/now")
        await conv.get_response(mark_read=True)
    try:
        ouvindo = await userge.get_inline_bot_results(
            "SpotifyNowBot", f"{(now)}."
        )
        await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=ouvindo.query_id,
            result_id=ouvindo.results.id,
            reply_to_message_id=message_id,
        )
    except IndexError:
        await message.err("Bacon")
