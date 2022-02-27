from userbot import CMD_HELP
from userbot.utils import skyzu_cmd

# FROM skyzu-userbot (https://github.com/Skyzu/skyzu-userbot)


@skyzu_cmd(pattern="(?:dm)\s?(.*)?")
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("`Success Mengirim Pesan Anda.`")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("`Success Mengirim Pesan Anda.`")
    except BaseException:
        await event.edit("**Terjadi Error. Gagal Mengirim Pesan.**")


@skyzu_cmd(pattern="open(?: |$)(.*)")
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    with open(b, "r") as a:
        c = a.read()
    await edit_or_reply(event, "**Berhasil Membaca Berkas**")
    if len(c) > 4095:
        await edit_or_reply(
            event, c, deflink=True, linktext="**Berhasil Membaca Berkas**"
        )
    else:
        await event.client.send_message(event.chat_id, f"`{c}`")
        await event.delete()
    os.remove(b)


CMD_HELP.update(
    {
        "message": "`.dm`\
    \nMengirim Pesan Dengan Jarak Jauh Dengan .dm <username> <pesan>."
    }
)
