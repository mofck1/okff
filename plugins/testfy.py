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
    if now:
        text = now
    elif spotify:
        text = now or spotify.text
    else:
        await message.err("Ovo!")
        return
    await message.delete()

    if "-n" in message.flags:
        await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=ouvindo.query_id,
            result_id=ouvindo.results.id,
            reply_to_message_id=message_id,
        )
    try:
        ouvindo = await userge.get_inline_bot_results(
            "SpotifyNowBot", f"{(text)}."
        )
        message_id = spotify.message_id if spotify else None
        await userge.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=ouvindo.query_id,
            result_id=ouvindo.results.id,
            reply_to_message_id=message_id,
        )
    except IndexError:
        await message.err("Bacon")
