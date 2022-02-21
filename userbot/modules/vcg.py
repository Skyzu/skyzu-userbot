# Thanks Full To Team Ultroid
# Ported By @skyzu

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import skyzu_cmd

NO_ADMIN = "`Maaf Kamu Bukan Admin!"


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


async def get_call(sky):
    sky = await sky.client(getchat(kyy.chat_id))
    await sky.client(getvc(sky.full_chat.call))
    return hehe.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@skyzu_cmd(pattern="startvc$")
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


@skyzu_cmd(pattern="stopvc$")
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


@skyzu_cmd(pattern="vcinvite")
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
        "vcg": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}startvc`\
         \n↳ : Start Group Call in a group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}stopvc`\
         \n↳ : `Stop Group Call in a group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vcinvite`\
         \n↳ : Invite all members of group in Group Call. (You must be joined)."
    }
)
