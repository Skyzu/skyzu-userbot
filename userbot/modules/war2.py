from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.sok(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**WOII**")
    sleep(2)
    await typew.edit("**NGENTOT**")
    sleep(1)
    await typew.edit("**KALO MENTAL MASIH PATUNGAN**")
    sleep(1)
    await typew.edit("**GAUSAH SOK KERAS DEH**")
    sleep(1)
    await typew.edit("**GAUSAH SOK KERAS DEH**")


