""" Teste """

import os
from userge import userge

@userge.on_cmd(
    "main",
    about={
        "header": "teste",
        "como usar": "{tr}main",
    },
    del_pre=True,
    allow_channels=False,
)
async def main_teste() -> None:
    chat_id = int(os.environ.get("CHAT_ID") or 0)
    type_ = 'unofficial' if os.path.exists("../userge/plugins/unofficial") else 'main'
    await userge.send_message(chat_id, f'`{type_} build completa`')

if __name__ == "__main__":
    userge.begin(_worker())
    print('Teste feito com sucesso. AppleBot')
