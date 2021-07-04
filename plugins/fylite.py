""" Módulo de testes para o @applled com fins de aprendizado """

 

from asyncio.exceptions import TimeoutError

from userge import Config, Message, get_collection, userge
from userge.utils.exceptions import StopConversation


@userge.on_cmd("fynow", about={
    'header': "Teste @applled",
    'como usar': "{tr}fynow "}, allow_via_bot=False)
async def fynow_(message: Message):
        async with userge.conversation("SpotifyNowBot") as conv:
            await conv.send_message("/start")
            await conv.send_message("/now")
            await conv.get_response(mark_read=True)
            try:
#               message = await conv.send_message()
                response = await conv.get_response()
 
            media = await message.client.download_media(replied, file_name=Config.DOWN_PATH)
                await message.client.send_photo(
                message.chat_id,
                file_name=media,
                force_document=False,
                caption=f"[Tocar no Spotify]({link})",
            )

            
            
            
            
#
#                await conv.get_response(mark_read=True)
#            ).text.split('\n', maxsplit=1)[-1]
#            await msg.edit(f"Prontinho: {shorten_url}", disable_web_page_preview=True)
#    except YouBlockedUser:
#        await msg.edit("Desbloqueie o **@SpotifyNowBot** ")
#    except StopConversation:
#        await msg.err("O Bot está morto...")
