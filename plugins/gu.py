from userge import userge, Message, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

LOG = userge.getLogger(__name__)  
CHANNEL = userge.getCLogger(__name__)  


@userge.on_cmd("gugu", about="Testes")
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
      
                owner = [
                    [
                        InlineKeyboardButton(
                            text="⚡️ Py 3.9.2 • Pyro 1.2.8", callback_data="info_btn"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="❎ UPDATE", callback_data="settings_btn"
                        ),
                        InlineKeyboardButton(text="🍏 INSPIRED", url=Config.MEUTG_REPO),
                    ],
                ]
                results.append(
                    InlineQueryResultPhoto(
                        photo_url="https://telegra.ph/file/a47baf0bfed24400c0089.png",
                        caption="Humm... ",
                        reply_markup=InlineKeyboardMarkup(owner),
                    )
                ) 
    
