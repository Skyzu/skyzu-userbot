from time import sleep
from platform import uname
from userbot import ALIVE_NAME, WEATHER_DEFCITY, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG LAH GOBLOKK!!!**")
# Pantun


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam Dulu Biar Sopan...`")
    sleep(2)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Salam


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
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
    await typew.edit("☑️ `askar Autis`")
    sleep(2)
    await typew.edit("✅ `askar Autis`")
    sleep(1)
    await typew.edit("`⚡ Cuma Skyzu Yang Paling Waras, Baik Hati, Dan Tidak Sombong :v`")
# King Userbot Support


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")
# Istigfar


@register(outgoing=True, pattern="^.alay(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Halo kak**")
    sleep(1)
    await typew.edit("**Gua liat-liat lu main bot mulu**")
    sleep(2)
    await typew.edit("**Alay banget sumpah**")
    sleep(2)
    await typew.edit("**Baru pasang ucelbot ya?**")
    sleep(2)
    await typew.edit("**Pantesan norak yahaha**")
    sleep(2)
    await typew.edit("**Kalo mau coba coba command di gc pribadi aja**")
    sleep(2)
    await typew.edit("**Jangan di publik, jijik liatnya anjg:v**")
    sleep(2)
    await typew.edit("**Intinya lo alay maen bot mulu**")
    sleep(2)
    await typew.edit("**Lawriiiiiiieeeee:v**")
# Alay maen bot mulu ngentot!


@register(outgoing=True, pattern="^.perkenalan(?: |$)(.*)")
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


CMD_HELP.update(
    {
        "gabut": "**Modules** - `Gabut`\
        \n\n Cmd : `.l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `.perkenalan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `.alay`\
        \nUsage : ngeledek orang baru pasang bot\
        \n\n Cmd : `.g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `.kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `.p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
