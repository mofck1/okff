from userge import userge, Message, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

LOG = userge.getLogger(__name__)  
CHANNEL = userge.getCLogger(__name__)  


@userge.on_cmd("gugu", about="Testes")
""" Teste """
async def test_cmd(message: Message):
   LOG.info("Seu teste foi iniciado, aguarde...")  
   await message.edit("Testando...", del_in=10)   
   await CHANNEL.log("Beleza, Gu!")   

@userge.on_filters(filters.me & filters.private)   
async def gugu_(message: Message):
   LOG.info("Iniciando o teste")
   await message.reply(f"Você digitou: {message.text}", del_in=5)
   applebot_pic = "https://telegra.ph/file/a47baf0bfed24400c0089.png"
   reply = message.reply_to_message
   reply_id = reply.message_id 
   await CHANNEL.log(".... Ok!")
   await message.client.send_photo(
   chat_id=message.chat.id, photo=applebot_pic, reply_to_message_id=reply_id
   )
      
      def gugu_buttons() -> InlineKeyboardMarkup:
        buttons = [
            [
                InlineKeyboardButton(text="⚡️ STATUS", callback_data="status_afk"),
                InlineKeyboardButton(text="Более", callback_data="status_apple"),
            ],
        ]
        return InlineKeyboardMarkup(buttons)  
    
