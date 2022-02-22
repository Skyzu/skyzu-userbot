# Edit By @skyzu

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import skyzu_cmd


@skyzu_cmd(pattern="thanks(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●\n"
        "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
        "╔══╦╗────╔╗─╔╗╔╗\n"
        "╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗\n"
        "─║║║║║╬║║║╩║╚╗╔╣║║║║\n"
        "─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\n"
        "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
        "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●"
    )


@skyzu_cmd(pattern="malam(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "╔═╦═╦╗╔═╦══╦═╦══╗\n"
        "║═╣═╣║║╬║║║║╬╠╗╔╝\n"
        "╠═║═╣╚╣║║║║║║║║║\n"
        "╚═╩═╩═╩╩╩╩╩╩╩╝╚╝\n\n"
        "╔══╦═╦╗╔═╦══╗\n"
        "║║║║╬║║║╬║║║║\n"
        "║║║║║║╚╣║║║║║\n"
        "╚╩╩╩╩╩═╩╩╩╩╩╝"
    )


@skyzu_cmd(pattern="rumah(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**GAMBAR RUMAH**\n"
        "╱◥◣\n"
        "│∩ │◥███◣ ╱◥███◣\n"
        "╱◥◣ ◥████◣▓∩▓│∩ ║\n"
        "│╱◥█◣║∩∩∩ ║◥█▓ ▓█◣\n"
        "││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║\n"
        "๑۩๑๑۩๑๑ ۩๑๑۩๑▓๑۩๑๑۩๑"
    )


CMD_HELP.update(
    {
        "animasi6": f"`{cmd}rumah` ; `{cmd}malam` ; `{cmd}thanks`\
    \nUsage: liat aja."
    }
)
