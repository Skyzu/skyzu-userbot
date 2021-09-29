from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.sok(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1.5)
    await typew.edit("**WOII**")
    sleep(1.5)
    await typew.edit("**KONTOL**")
    sleep(1.5)
    await typew.edit("**KALO MENTAL MASIH PATUNGAN**")
    sleep(1.5)
    await typew.edit("**GAUSAH SOK KERAS DEH**")
    sleep(1.5)
    await typew.edit("**GA KEREN LO BEGITU NGENTOT**")


CMD_HELP.update(
    {
        "war2": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .sok\
         \n↳ : ngatain orang yang sok keras\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .gucast\
         \n↳ : Mengirim Pesan Pribadi Secara Global"
    }
)
