""" Módulo de testes para o @applled com fins de aprendizado """

import os
from pyrogram.errors import YouBlockedUser
from userge import Config, Message, userge
from userge.utils.exceptions import StopConversation, progress


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
            # await msg.edit(f"{resultado}") # Inicio                     
            
    spot = await message.client.download_media(
        message=message.reply_to_message,
        file_name=Config.DOWN_PATH,
        progress=progress,
        progress_args=(message, "Aguarde..."),
    )
    await message.edit("`Só mais um pouco...`")
    try:
        response = upload_file(spot)
    except Exception as t_e:
        await message.err(t_e)
        return
    os.remove(dl_loc)
    return str(response[0])
            
            
    except YouBlockedUser: # Fim
        await msg.edit("Desbloqueie o **@SpotipieBot**")
    except StopConversation:
        await msg.err("O Bot está morto...")
