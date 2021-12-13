# Thanks Full To Team Ultroid
# Ported By @skyzu

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`Maaf Kamu Bukan Admin!"


async def get_call(event):
    geez = await event.client(getchat(event.chat_id))
    vcky = await event.client(getvc(geez.full_chat.call))
    return vcky.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@register(outgoing=True, pattern=r"^\.startvc$", groups_only=True)
async def start_voice(td):
    chat = await td.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await td.edit(NO_ADMIN)
    try:
        await td.client(startvc(td.chat_id))
        await td.edit("`Voice Chat Started...`")
    except Exception as ex:
        await td.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.stopvc$", groups_only=True)
async def stop_voice(td):
    chat = await td.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await td.edit(NO_ADMIN)
    try:
        await td.client(stopvc(await get_call(td)))
        await td.edit("`Voice Chat Stopped...`")
    except Exception as ex:
        await td.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.vcinvite", groups_only=True)
async def vc_invite(td):
    await td.edit("`Sedang Mengivinte Member...`")
    users = []
    z = 0
    async for x in td.client.iter_participants(td.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await td.client(invitetovc(call=await get_call(td), users=p))
            z += 6
        except BaseException:
            pass
    await td.edit(f"`Invited {z} users`")


CMD_HELP.update(
    {
        "vcg": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startvc`\
         \n↳ : Start Group Call in a group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopvc`\
         \n↳ : `Stop Group Call in a group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcinvite`\
         \n↳ : Invite all members of group in Group Call. (You must be joined)."
    }
)
