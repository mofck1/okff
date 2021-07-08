""" Módulo de testes para o @applled com fins de aprendizado """
""" Sua exibição ainda está em testes """


import datetime
import asyncio
import os
from pyrogram.errors import YouBlockedUser
from userge import Config, Message, userge
from userge.utils.exceptions import StopConversation

@userge.on_cmd("citar", about={
    'header': "Teste do @applled",
    'como usar': "{tr}citar"}, 
               
    allow_via_bot=False, 
    allow_channels=False,
              )

async def citar(msg: Message):
    if not msg.reply_to_message_id:
       await msg.edit("```Responda a qualquer mensagem.```")
       return
    reply_message = await msg.get_reply_message() 
    if not reply_message.text:
       await msg.edit("```Responda a uma mensagem com texto```")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await msg.edit("```Responde a mensagens de pessoas reais.```")
       return
    await msg.edit("```Fazendo uma citação...```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_message(msg.NewMessage(incoming=True,from_users=830103832))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await msg.reply("```Desbloqueie o @QuotLyBot```")
              return
          if response.text.startswith("Ei!"):
             await msg.edit("```Configure certinho a privacidade das mensagens.```")
          else: 
             await msg.delete()   
             await bot.forward_messages(msg.chat_id, response.message)
