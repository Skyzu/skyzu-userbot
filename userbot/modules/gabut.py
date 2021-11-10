from platform import uname
from time import sleep

from userbot import ALIVE_NAME, CMD_HELP, WEATHER_DEFCITY
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.g(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG LAH GOBLOKK!!!**")


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


@register(outgoing=True, pattern="^.kenalin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `putra wibu`")
    sleep(2)
    await typew.edit("✅ `putra wibu`")
    sleep(1)
    await typew.edit("☑️ `duta stres`")
    sleep(2)
    await typew.edit("✅ `duta stres`")
    sleep(1)
    await typew.edit("☑️ `fajar Gajelas`")
    sleep(2)
    await typew.edit("✅ `fajar Gajelas`")
    sleep(1)
    await typew.edit("☑️ `ken Wibu Sangean`")
    sleep(2)
    await typew.edit("✅ `ken Wibu Sangean`")
    sleep(1)
    await typew.edit("☑️ `xxinu Autis`")
    sleep(2)
    await typew.edit("✅ `xxinu Autis`")
    sleep(1)
    await typew.edit(
        "`⚡ Cuma Skyzu Yang Paling Waras, Baik Hati, Dan Tidak Sombong :v`"
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


@register(outgoing=True, pattern="^.perkenalkan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")


# Perkenalan


@register(outgoing=True, pattern="^.skyzu(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Ehh Lu Mau Tau Gak?**")
    sleep(1)
    await typew.edit("**Sih Skyzu mukanya mirip babi😂**")
    sleep(1)
    await typew.edit("**Ehh Gak Bercanda Deh😁**")
    sleep(1)
    await typew.edit("**Emang Bener Sih Skyzu Mukanya Kaya Babi🙈**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh,Skyzu Kan Ganteng Kaya Artis Korea😄**")
    sleep(1)
    await typew.edit("**Tapi Boong😂**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Skyzu Nangis Minta Balon😂**")
    sleep(1)
    await typew.edit("**Maaf Ya Skyzu Ganteng Bercanda😁**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")


# Create by myself @skyzuex


CMD_HELP.update(
    {
        "gabut": "**Modules** - `Gabut`\
        \n\n Cmd : `.l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `.perkenalkan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `.virtual`\
        \nUsage : ngeledek orang yang virtual\
        \n\n Cmd : `.g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `.kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `.skyzu`\
        \nUsage : buat ngeledek skyzu\
        \n\n Cmd : `.p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
