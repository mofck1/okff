# plugin for USERGE-X made by @Kakashi_HTK(tg)/@ashwinstr(gh) Adaptado or Apple @applled
# v1.3.3


from pyrogram.raw.functions.account import ReportPeer
from pyrogram.raw.types import InputReportReasonPornography, InputReportReasonSpam, InputPeerUserFromMessage

from userge import userge, Message, Config

CHANNEL = userge.getCLogger(__name__)


@userge.on_cmd(
    "rep",
    about={
        "títuo": "Reportar um usuário por spam",
        "descrição": "Reporte usuários por spam",
        "como usar": "{tr}rep [spam (padrão)] ou [nsfw (caso seja conteúdo adulto)(opcional)] [só responder uma mensagem com o comando]\n"
    },
)
async def reportar(message: Message):
    """Reportar um usuário por spam"""
    reply_ = message.reply_to_message
    if not reply_:
        await message.edit("`Reportar o vento?\nUse o comando como resposta na mensagem de spam.`")
        return 
    await message.edit("`Verificando o usuário...`")
    user_ = await userge.get_users(reply_.from_user.id)
    me_ = await userge.get_me()
    if user_.id in (Config.SUDO_USERS or Config.OWNER_ID) or user_.id == me_.id:
        await message.edit(f"Não posso reportar o usuário <b>{user_.mention}</b>, pois está configurado em seu SUDO...", del_in=5)
        return
    reason_ = message.input_str
    if reason_ == "nsfw":
        reason_ = InputReportReasonPornography()
        for_ = "<b>Conteúdo</b> adulto"
    else:
        reason_ = InputReportReasonSpam()
        for_ = "Mensagem de <b>Spam</b>"
    peer_ = InputPeerUserFromMessage(
        peer=message.chat.id,
        msg_id=reply_.message_id,
        user_id=user_.id,
    ),
    ReportPeer(
        peer=peer_,
        reason=reason_,
        message=reply_,
    )
    msg_ =  (
        "⚠️ <b>Usuário Reportado</b> ⚠️\n\n"
        f"<b>— Quem?</b> {user_.mention}\n\n"
        f"<b>— Motivo:</b> <i>{for_}</i>"
    )
    await message.edit(msg_)
    await CHANNEL.log(msg_)
       
