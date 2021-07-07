""" Módulo de testes para o @applled com fins de aprendizado """


from pyrogram.errors import YouBlockedUser
from userge import userge, Message
from userge.utils.exceptions import StopConversation


@userge.on_cmd("gusta", about={
    'header': "Teste do @applled",
    'como usar': "{tr}gusta"}, allow_via_bot=False)
async def gusta(msg: Message):
    chat = "/now" # msg.input_or_reply_str
    if not chat:
        await msg.err("Erro.")
        return
    try:
        async with userge.conversation("SpotipieBot") as conv:
            await conv.send_message("/start")
            await conv.get_response(mark_read=True)
            await conv.send_message(chat)
            resultado = (
                await conv.get_response(mark_read=True)
            ) #.text.split('\n', maxsplit=1)[-1]
            await msg.edit(f"{resultado}") # Inicio
                       if response.text.startswith("You're"):
                await msg.edit(
                    "**Você não está ouvindo nada no Spotify no momento.**"
                )
                return
            downloaded_file_name = await message.client.download_media(
                response.media, DOWN_PATH
            )
            link = response.reply_markup.rows[0].buttons[0].url
            await message.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                caption=f"[Tocar no Spotify]({link})",
            )
    except YouBlockedUser: # Fim
        await msg.edit("Desbloqueie o **@SpotipieBot**")
    except StopConversation:
        await msg.err("O Bot está morto...")
