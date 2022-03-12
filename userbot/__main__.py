# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

from userbot import (
    ALIVE_NAME,
    BOT_TOKEN,
    BOT_USERNAME,
    BOT_VER,
    BOTLOG_CHATID,
    LOGS,
    UPSTREAM_REPO_BRANCH,
    bot,
    call_py,
)
from userbot.modules import ALL_MODULES
from userbot.utils import autobot
from userbot.utils.tools import ya_kali_ngga

try:
    for module_name in ALL_MODULES:
        imported_module = import_module("userbot.modules." + module_name)
    bot.start()
    call_py.start()
    user = bot.get_me()
    LOGS.info(f"⚡Skyzu-Userbot⚡ ⚙️ V{BOT_VER} [ TELAH DIAKTIFKAN! ]")
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


async def userbot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"⚡Userbot berhasil di aktifkan\n━━━━━━━━━━━━━━━\n❃ Bot Of : {ALIVE_NAME}\n❃ BotVer : {BOT_VER}@{UPSTREAM_REPO_BRANCH}\n━━━━━━━━━━━━━━━",
            )
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass


bot.loop.run_until_complete(userbot_on())
bot.loop.run_until_complete(ya_kali_ngga())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars tidak terisi, Memulai Membuat BOT Otomatis di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
