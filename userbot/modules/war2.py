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


@register(outgoing=True, pattern=r"^\.an(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LO KAN HASIL ZINAH HASIL HUB TERLARANG NAH LO DI BUANG DI TONGSAMPAH NAH MAK LO YG SKRG KASIAN SAMA LO MKNY DI PUNGUT UDH LO CACAT KAKI CACAT TANGAN CACAT MUKA CACAT SEMUAHNY PARAH BET SI KONTOL LO JUGA CACATAN PASTI NANAHAN JUGA,UDH MENDING LO BUNDIR DEH JADI BEBAN ORG DOANG BEGO NGERUGIN MASYARKAT BEGO BOCAH HINA BOCAH HARAM BOCAH AUTIS KEK LO MENDING MATI AJA**")


CMD_HELP.update(
    {
        "war2": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .sok\
         \n↳ : ngatain orang yang sok keras\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .an\
         \n↳ : ngatain anak pungut"
    }
)
