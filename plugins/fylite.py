""" Módulo de testes para o @applled com fins de aprendizado """

 

from asyncio.exceptions import TimeoutError

from userge import Config, Message, get_collection, userge
from userge import DOWN_PATH, bot
from pyrogram.errors import YouBlockedUser
from userge.utils.exceptions import StopConversation


@userge.on_cmd("fynow", about={
    'header': "Teste @applled",
    'como usar': "{tr}fynow "}, allow_via_bot=False)
async def bitly(msg: Message):
    now = "/now"
    if not now:
        await msg.err("Algo de errado não está certo.")
        return
    try:
        async with userge.conversation("SpotifyNowBot") as conv:
            await conv.send_message("/start")
            await conv.get_response(mark_read=True)
            try:
                msg = await conv.send_message(now)
                response = await conv.get_response()
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await message.reply("**Por favor desbloqueie** @SpotifyNowBot**.**")
                return
            if response.text.startswith("You're"):
                await message.edit(
                    "**Você não está ouvindo nada no Spotify no momento.**"
                )
                return
            downloaded_file_name = await message.client.download_media(
                response.media, DOWN_PATH
            )
            link = response.reply_markup.rows[0].buttons[0].url
            await message.client.send_file(
                message.chat_id,
                downloaded_file_name,
                force_document=False,
                caption=f"[Tocar no Spotify]({link})",
            )
            await message.client.delete_messages(conv.chat_id, [msg.id, response.id])
    except TimeoutError:
        return await message.edit("**Erro:** @SpotifyNowBot **não está respondendo.**")
    await message.delete()
    return os.remove(downloaded_file_name)
            
            
            
            
#
#                await conv.get_response(mark_read=True)
#            ).text.split('\n', maxsplit=1)[-1]
#            await msg.edit(f"Prontinho: {shorten_url}", disable_web_page_preview=True)
#    except YouBlockedUser:
#        await msg.edit("Desbloqueie o **@SpotifyNowBot** ")
#    except StopConversation:
#        await msg.err("O Bot está morto...")
