""" Módulo teste de velocidade para o @applled """

import os

import speedtest
import wget

from userge import Message, userge
from userge.utils import humanbytes

@userge.on_cmd(
    "speed",
    about={
        "header": "Módulo teste de velocidade para o @applled",
    },
    del_pre=True,
    allow_channels=False,
)

async def spee_test(message: Message):
    ms_g = await message.edit(message, "`Por favor, aguarde... \nCalculando velocidade de conexão com o servidor.`")
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    img_ = s.results.share()
    _neat_test = f"""<b><u>Resultado do TESTE DE VELOCIDADE</b></u>
    
▶ <b>IP:</b> <code>{client_infos['ip']}</code>
▶ <b>ISP:</b> <code>{client_infos['isp']}</code>
▶ <b>País:</b> <code>{client_infos['country']}</code>
▶ <b>Download:</b> <code>{convert_from_bytes_to_human_formats(download_speed)}</code>
▶ <b>Upload:</b> <code>{convert_from_bytes_to_human_formats(upload_speed)}</code>
▶ <b>ISP RATING :</b> <code>{client_infos['isprating']}</code>
▶ <b>PING TIME :</b> <code>{ping_time}</code>
"""
    if img_:
      if message.reply_to_message:
        await client.send_photo(
            message.chat.id,
            img_,
            reply_to_message_id=message.reply_to_message.message_id,
            caption=_neat_test
        )
      else:
        await client.send_photo(
            message.chat.id,
            img_,
            caption=_neat_test
            )
      await ms_g.delete()
    else:
      await ms_g.edit(_neat_test)


def convert_from_bytes_to_human_formats(size):
    power = 2**10
    n = 0
    units = {
        0: "",
        1: "KB",
        2: "MB",
        3: "GB",
        4: "TB"
    }
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"
