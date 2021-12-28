# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("`Command` **Tidak Valid**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t ❉  "
        await event.edit(
            "**⚡𝐒𝐊𝐘𝐙𝐔-𝐔𝐒𝐄𝐑𝐁𝐎𝐓​⚡**\n\n"
            f"**◉ Bᴏᴛ ᴏꜰ {DEFAULTUSER}**\n**◉ Mᴏᴅᴜʟᴇꜱ : {len(modules)}**\n\n"
            "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
            f"◉ {string}◉\n\n✐ **ɴᴏᴛᴇꜱ :**  `.help animasi`\n✐  support : @skyzusupport"
        )
        await asyncio.sleep(1000)
        await event.delete()
