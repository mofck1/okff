""" Módulo de testes para o @applled com fins de aprendizado """
""" Sua exibição ainda está em testes """

from userge import Message, userge
from userge.utils import deEmojify


@userge.on_cmd(
    "ffy",
    about={
        "titulo": "Teste",
        "como usar": "{tr}ffy\n",
        "examples": ["{tr}ffy"],
    },
    allow_via_bot=False,
)
async def meu_ovo(message: Message):
    """ Teste para o Apple """
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
    if "-g" in message.flags:
        try:
            stickers = await userge.get_inline_bot_results(
                "SpotipieBot", f"{deEmojify(text)}"
            )
            await userge.send_inline_bot_result(
                chat_id=message.chat.id,
                query_id=stickers.query_id,
                result_id=stickers.results[0].id,
                hide_via=True,
            )
