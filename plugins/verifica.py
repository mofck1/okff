""" Teste do Apple para aprendizado """


from pyrogram.raw import types, functions
from userge.utils import mention_html
from userge import Message, userge


@userge.on_cmd(
    "verifica",
    about={
        "header": "Teste.",
        "como usar": "{tr}verifica",
    },
)
async def verifica_(message: Message):
chat = 'inlineApple'
chat_name = (await userge.get_chat(chat)).title
new_users = (await userge.send(functions.channels.GetAdminLog(
    channel=await userge.resolve_peer(chat),
    q="",
    events_filter=types.ChannelAdminLogEventsFilter(join=True),
    max_id=0,
    min_id=0,
    limit=100
))).users
output_ = f"<b><u>Membros recentes no Grupo:</u></b>\n**{chat_name}**\n"
for user in new_users:
    name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
    if name:
        output_ += "• {}\n".format(mention_html(user.id, name))
    else:
        output_ += "• {}\n".format(mention_html(user.id, '[no name]'))
await message.reply(output_)
