from platform import uname
from time import sleep

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, WEATHER_DEFCITY
from userbot.utils import skyzu_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@skyzu_cmd(pattern="g(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG LAH GOBLOKK!!!**")


# Pantun


@skyzu_cmd(pattern="p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam Dulu Biar Sopan...`")
    sleep(2)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Salam


@skyzu_cmd(pattern="l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kalo Orang Salam Itu Dijawab...`")
    sleep(2)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Menjawab Salam


@skyzu_cmd(pattern="kenalin(?: |$)(.*)")
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


@skyzu_cmd(pattern="istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")


# Istigfar


@skyzu_cmd(pattern="virtual(?: |$)(.*)")
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


@skyzu_cmd(pattern="perkenalkan(?: |$)(.*)")
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


@skyzu_cmd(pattern="skyzu(?: |$)(.*)")
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
        "gabut": f"**Modules** - `Gabut`\
        \n\n Cmd : `{cmd}l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `{cmd}perkenalkan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `{cmd}virtual`\
        \nUsage : ngeledek orang yang virtual\
        \n\n Cmd : `{cmd}g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `{cmd}kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `{cmd}skyzu`\
        \nUsage : buat ngeledek skyzu\
        \n\n Cmd : `{cmd}p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
