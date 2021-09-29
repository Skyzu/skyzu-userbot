from time import sleep

from userbot.events import register


@register(outgoing=True, pattern=r"^\.sok(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1.5)
    await typew.edit("**WOII**")
    sleep(1.5)
    await typew.edit("**NGENTOT**")
    sleep(1.5)
    await typew.edit("**KALO MENTAL MASIH PATUNGAN**")
    sleep(1.5)
    await typew.edit("**GAUSAH SOK KERAS DEH**")
    sleep(1.5)
    await typew.edit("**GAUSAH SOK KERAS DEH**")
