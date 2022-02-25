# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for executing code and terminal commands from Telegram. """

import asyncio
import io
import re
import sys
import traceback
from getpass import getuser
from os import remove

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, TERM_ALIAS
from userbot.utils import skyzu_cmd


@skyzu_cmd(pattern="eval(?:\s|$)([\s\S]*)")
async def _(event):
    expression = event.pattern_match.group(1)
    if not expression:
        return await event.edit("**Berikan Code untuk di eksekusi.**")
    if expression in ("userbot.session", "config.env"):
        return await event.edit("**Itu operasi yang berbahaya! Tidak diperbolehkan!**")
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not cmd:
        return event.edit("**Apa yang harus saya jalankan?**")
    cmd = (
        cmd.replace("sendmessage", "send_message")
        .replace("sendfile", "send_file")
        .replace("editmessage", "edit_message")
    )
    xx = await event.edit("`Processing...`")
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    reply_to_id = event.message.id

    async def aexec(code, event):
        exec(
            "async def __aexec(e, client): "
            + "\n message = event = e"
            + "\n reply = await event.get_reply_message()"
            + "\n chat = (await event.get_chat()).id"
            + "".join(f"\n {line}" for line in code.split("\n")),
        )

        return await locals()["__aexec"](event, event.client)

    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = f"**•  Eval : **\n`{cmd}` \n\n**•  Result : **\n`{evaluation}` \n"

    if len(final_output) > 4096:
        man = final_output.replace("`", "").replace("**", "").replace("__", "")
        with io.BytesIO(str.encode(man)) as out_file:
            out_file.name = "eval.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                thumb="userbot/resources/logo.jpg",
                allow_cache=False,
                caption=f"`{cmd}`" if len(cmd) < 998 else None,
                reply_to=reply_to_id,
            )
            await xx.delete()
    else:
        await xx.edit(final_output)


@skyzu_cmd(pattern="term(?: |$|\n)(.*)")
async def terminal_runner(term):
    """For .term command, runs bash commands and scripts on your server."""
    curruser = TERM_ALIAS if TERM_ALIAS else getuser()
    command = term.pattern_match.group(1)
    try:
        from os import geteuid

        uid = geteuid()
    except ImportError:
        uid = "This ain't it chief!"

    if term.is_channel and not term.is_group:
        return await term.edit("`Term commands aren't permitted on channels!`")

    if not command:
        return await term.edit(
            "``` Give a command or use .help term for an example.```"
        )

    for i in ("userbot.session", "env"):
        if command.find(i) != -1:
            return await term.edit("`That's a dangerous operation! Not Permitted!`")

    if not re.search(r"echo[ \-\w]*\$\w+", command) is None:
        return await term.edit("`That's a dangerous operation! Not Permitted!`")

    process = await asyncio.create_subprocess_shell(
        command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    if len(result) > 4096:
        output = open("output.txt", "w+")
        output.write(result)
        output.close()
        await term.client.send_file(
            term.chat_id,
            "output.txt",
            reply_to=term.id,
            caption="`Output too large, sending as file`",
        )
        remove("output.txt")
        return

    if uid == 0:
        await term.edit(f"`{curruser}:~# {command}\n{result}`")
    else:
        await term.edit(f"`{curruser}:~$ {command}\n{result}`")


@skyzu_cmd(pattern="json$")
async def _(event):
    if event.fwd_from:
        return
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    if len(the_real_message) > 4096:
        with io.BytesIO(str.encode(the_real_message)) as out_file:
            out_file.name = "json.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                thumb="userbot/resources/logo.jpg",
                allow_cache=False,
                reply_to=reply_to_id,
            )
            await event.delete()
    else:
        await event.edit("`{}`".format(the_real_message))


CMD_HELP.update(
    {
        "eval": f">`{cmd}eval print('world')`" "\nUsage: Just like exec.",
        "exec": f">`{cmd}exec print('hello')`" "\nUsage: Execute small python scripts.",
        "term": f">`{cmd}term <cmd>`"
        "\nUsage: Run bash commands and scripts on your server.",
    }
)
