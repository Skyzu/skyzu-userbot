from platform import uname
from time import sleep

from userbot import ALIVE_NAME, CMD_HELP, WEATHER_DEFCITY
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.av(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**AV NIH BOS**")
    sleep(3)
    await typew.edit("**MENG AV AV DULU GA SEH**")
    sleep(2)
    await typew.edit("**LEPIN SI PALING GANTENG**")
    sleep(1)
    await typew.edit("**ODEN SI BAPAK OWNER**")
    sleep(1)
    await typew.edit("**FUCKIH CHINDO HUNTER**")
    sleep(1)
    await typew.edit("**ARSI SI PETARUNK**")
    sleep(1)
    await typew.edit("**LEMME UNLIMITED KOSA KATA**")
    sleep(1)
    await typew.edit("**ZENE SI BROTHER TEGAR**")
    sleep(1)
    await typew.edit("**REPAN SI PALING RAPPER**")
    sleep(1)
    await typew.edit("**NIMO SI TALENT BD**")
    sleep(1)
    await typew.edit("**BOBY S3 PROMOTE CH**")
    sleep(1)
    await typew.edit("**UCOK KEMBARAN CJ GTA**")
    sleep(1)
    await typew.edit("**YANG GA KESEBUT MAAF YA CAPE EDITNYA NGENTOT**")
    sleep(2)
    await typew.edit("**LOPYU CIWAY CIWAY ANGVI KALIAN CANTIK CANTIK**")
    sleep(2)
    await typew.edit("**SEKIAN TERIMA KASIH**)
    sleep(2)
    await typew.edit("**© @levindyno**")

# Pantun


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam Dulu Biar Sopan...`")
    sleep(2)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Salam


@register(outgoing=True, pattern="^.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kalo Orang Salam Itu Dijawab...`")
    sleep(2)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Menjawab Salam


@register(outgoing=True, pattern="^.iapin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `Lepin Wibu`")
    sleep(2)
    await typew.edit("✅ `Lepin Wibu`")
    sleep(1)
    await typew.edit("☑️ `Lepin Stres`")
    sleep(2)
    await typew.edit("✘ `Lepin stres`")
    sleep(1)
    await typew.edit("☑️ `Lepin Gajelas`")
    sleep(2)
    await typew.edit("✅ `Lepin Gajelas`")
    sleep(1)
    await typew.edit("☑️ `Lepin Wibu Sangean`")
    sleep(2)
    await typew.edit("✘ `Lepin Wibu Sangean`")
    sleep(1)
    await typew.edit("☑️ `Lepin Perfect`")
    sleep(2)
    await typew.edit("✅ `Lepin Perfect`")
    sleep(1)
    await typew.edit(
        "`⚡ Itu semua cuma kebohongan, Jangan di anggap serius brodi`"
    )


# King Userbot Support


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")


# Istigfar


@register(outgoing=True, pattern=r"^\.virtual(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**OOOO**")
    sleep(1.5)
    await typew.edit("**INI YANG VIRTUAL**")
    sleep(1.5)
    await typew.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await typew.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await typew.edit("**NI INGET**")
    sleep(1.5)
    await typew.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await typew.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await typew.edit("**BHAHAHAHA**")
    sleep(1.5)
    await typew.edit("**KASIAN MANA MASIH MUDA**")


@register(outgoing=True, pattern="^.terlepin(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit("`terlepin lepin dulu`")
    sleep(2)
    await event.edit("`Pertama Tama`")
    sleep(1.2)
    await event.edit("`Lepin Ganteng`")
    sleep(1)
    await event.edit("`Keren`")
    sleep(1)
    await event.edit("`Tidak Sombong`")
    sleep(1)
    await event.edit("`Manis`")
    sleep(1)
    await event.edit("`Penyayang`")
    sleep(1)
    await event.edit("`Sekian Dan Terima Kasih Buat Lo Semua`")
    sleep(1)
    await event.edit("`NGENTOT`")
    sleep(1)
    await event.edit("`Create By Lepin Keren`")
    


# Perkenalan


@register(outgoing=True, pattern="^.phd(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Ehh Lu Mau Tau Gak?**")
    sleep(1)
    await typew.edit("**Pitsa Ivangel Cantik Banget Anjir**")
    sleep(1)
    await typew.edit("**Sumpah Gak Bohong**")
    sleep(1)
    await typew.edit("**Emang Bener Sih Pitsa Spek Bidadari**")
    sleep(1)
    await typew.edit("**Ehh Tapi Engga Deh,Ada Kartun Yang Harus Aku Jaga😅**")
    sleep(1)
    await typew.edit("**Tapi Boong😂**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Phd Marah Minta Bobba😂**")
    sleep(1)
    await typew.edit("**Maaf Ya Pitsa Cantik Bercanda😁**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")


# Create by myself @skyzuex




CMD_HELP.update(
    {
        "gabut": "**Modules** - `Gabut`\
        \n\n Cmd : `.l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `.terlepin`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `.virtual`\
        \nUsage : ngeledek orang yang virtual\
        \n\n Cmd : `.av`\
        \nUsage : ALL ABOUT AV\
        \n\n Cmd : `.iapin`\
        \nUsage : Awokwok\
        \n\n Cmd : `.phd`\
        \nUsage : buat ngeledek pitsa\
        \n\n Cmd : `.p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
