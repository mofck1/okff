""" @Applled - Lindo e maravilhoso """

import asyncio
import random
from userge import Message, userge
@userge.on_cmd(
    "pro",
    about={
        "título": "Tu sabe o que é :D",
        "como usar": "{tr}só mandar reply",
    },
)
async def proton_msg(message: Message):
  await message.edit(f"""<i>ⓘ Essa mensagem está disponível apenas para usuários da ProtonAOSP Premium.</i> <u>[Saiba mais](https://bit.ly/protonpremium)</u>""")
  
  
  
  