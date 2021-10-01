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


@register(outgoing=True, pattern=r"^\.bk(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BUAT LO KONTOL NIH KALO UDAH HINA GAUSAH SOK SOK NGEHINA HINA GUA KONTOL, GUA TERLALU SUCI BUAT LU YANG HINA ITU ADUHHH. SINI GUA LUDAHIN DLU LU BIAR DIRI LU SUCI KARENA LU TAU LUDAH GUA ITU MULIA SEKALI**")


@register(outgoing=True, pattern=r"^\.gj(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**YA AMPUN LU NGOMONG APA? GA NYAMBUNG KONTOL KAYA KEHIDUPAN LU MAKANYA ORG ORG KAYA LU GABAKALN MAJU HIDUPNYA APA LAGI ORG ORG BAWAHAN KAYA LU.**")


@register(outgoing=True, pattern='^.title(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**OI ANAK TITLE**")
    sleep(2)
    await typew.edit("**OOO INI YANG SOK JADI PAHLAWAN DI TELEGRAM?**")
    sleep(3)
    await typew.edit("**TITLE KEMANA MANA SAMPE MENUHIN NAMA**")
    sleep(2)
    await typew.edit("**ADA YANG SAMPE 18+ LAH SEGALA MACEM**")
    sleep(2)
    await typew.edit("**LO KIRA KEREN KEK GITU?**")
    sleep(2)
    await typew.edit("**KERJAAN CUMA NGURUSIN GRUP DI TELEGRAM SAMA NGAJAK ORANG WAR**")
    sleep(4)
    await typew.edit("**YAELAH BRO MENTAL LO CUMA DI SOSMED APA GIMANE?**")
    sleep(2)
    await typew.edit("**PERASAAN DULU TELEGRAM GAADA DEH BOCAH BOCAH SOK JAGO KEK GINI**")
    sleep(2)
    await typew.edit("**GILIRAN TITLE NYA DI EJEK NGADU KE OWNER NYA**")
    sleep(4)
    await typew.edit("**TRUS NGAJAK WAR**")
    sleep(2)
    await typew.edit("**BUSET DAH BANG**")
    sleep(2)
    await typew.edit("**UDAH SEJAGO APESI SAMPE GC DIBELA BELA**")
    sleep(3)
    await typew.edit("**ORANG TUA LO NOH ADA YANG NAGIH UTANG UDA LO BELA BELOM?**")
    sleep(4)
    await typew.edit("**RELA NGUTANG DEMI NGIDUPIN LU**")
    sleep(2)
    await typew.edit("**EH ANAKNYA MALAH NGEBELAIN GC GAJELAS HAHAHA**")
    sleep(3)
    await typew.edit("**MANA VIRTUAL LAGI, SOK JAGO LAGI DUH**")
    sleep(3)
    await typew.edit("**SEMOGA CEPET SADAR YA HAHAHAHA**")


CMD_HELP.update(
    {
        "war2": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .sok\
         \n↳ : ngatain orang yang sok keras\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .bk\
         \n↳ : ngatain bocah hina\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .gj\
         \n↳ : ngatain bocah gajelas\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .title\
         \n↳ : ngatain bocah gila title\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .an\
         \n↳ : ngatain anak pungut"
    }
)
