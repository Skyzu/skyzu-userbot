from userbot import CMD_HELP, bot
form userbot import CMD_HANDLER
from userbot.utils import skyzu_cmd


@skyzu_cmd(pattern="xogame(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


@skyzu_cmd(pattern="whisp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()


@skyzu_cmd(pattern="mod(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()


CMD_HELP.update(
    {
        "games": "\
𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.xogame`\
\n↳ : Mainkan game XO bersama temanmu.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.mod <nama app>`\
\n↳ : Dapatkan applikasi mod\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.whisp <teks> <username/ID>`\
\n↳ : Berikan pesan rahasia"
    }
)
