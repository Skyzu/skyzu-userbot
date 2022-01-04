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
    sleep(3)
    await typew.edit("**DAR DER DOR MENTAL LU GUA GEDOR**") 
    sleep(4) 


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`ASSALAMUALAIKUM ANAK NGENTOT`")
    sleep(2)
    await typew.edit("`ASSALAMUALAIKUM ANAK BABI`")
    sleep(2)

# Salam


@register(outgoing=True, pattern="^.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`WAALAIKUMSALAM,JADI NGENTOT GA? `")
    sleep(2)
    await typew.edit("`WAALAIKUMSALAM KONTOL`")
    sleep(2) 


# Menjawab Salam


@register(outgoing=True, pattern="^.kenal(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `Barra jelek`")
    sleep(2)
    await typew.edit("✅ `Barra jelek`")
    sleep(1)
    await typew.edit("☑️ `Cenna goblok`")
    sleep(2)
    await typew.edit("✅ `Cenna goblok`")
    sleep(1)
    await typew.edit("☑️ `Skyzu Kang Coli`")
    sleep(2)
    await typew.edit("✅ `Skyzu Kang Coli`")
    sleep(1)
    await typew.edit("☑️ `Cumii cantik`")
    sleep(2)
    await typew.edit("✅ `Cumii cantik`")
    sleep(1)
    await typew.edit("☑️ `Vxin cina bego`")
    sleep(2)
    await typew.edit("✅ `Vxin cina bego`")
    sleep(1)
    await typew.edit(
        "`CUMA JOO YANG PALING KEREN NGENTOT!!`"
    )


# King Userbot Support


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Astaghfirullah ya Tuhan yesus`")
    sleep(2)
    await event.edit("`itu titit ya anjing`")
    sleep(2) 

# Istigfar


@register(outgoing=True, pattern=r"^\.jelek(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EHH GOBLOK LU JELEK**")
    sleep(2.5)
    await typew.edit("**GAUSA SOSOAN NGEGHOSTING TOLOL**")
    sleep(2.5)
    await typew.edit("**MUKA LU AJA DEKIL GOBLOK**")
    sleep(2.5)
    await typew.edit("**SADAR TOLOL LU JELEK**")
    sleep(2.5)
    await typew.edit("**UDAH JELEK NYAKITIN GOBLOK**")
    sleep(2.5)
    await typew.edit("**DASAR ANAK NGENTOT**")
    sleep(2.5)
    await typew.edit("**DAKI DIMANA MANA**")
    sleep(2.5)
    await typew.edit("**KALO LU JELEK**")
    sleep(2.5)
    await typew.edit("**MINIMAL MANDILAH KONTOL**")


@register(outgoing=True, pattern="^.perkenalkan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Ngentot , Perkenalkan Nama Gua {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gua Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Jangan Lupa Coli Kontol`")
    sleep(2)
    await event.edit("`Udah Yatim Mending Diem`")


# Perkenalan


@register(outgoing=True, pattern="^.kalem(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**DARR DERR DORR**")
    sleep(2)
    await typew.edit("**STELL KALEM MINTA DI GEDOR**")
    sleep(2)
    await typew.edit("**KUKIRA SITU KERAS🥺**")
    sleep(2)
    await typew.edit("**TERNYATA KERTAS**")
    sleep(2)
    await typew.edit("**AWOKAWOKAWOK**")
    sleep(2)
    await typew.edit("**UDAH GOBLOK**")
    sleep(2)
    await typew.edit("**CIRCLE STELL KALEM PALING OP**")
    sleep(2)
    await typew.edit("**INDEPENDENT NIH BOS**")
    sleep(2)
    await typew.edit("**ANTI KUBU KUBU TAI ANJING**")
    sleep(2)
    await typew.edit("**INTINYA KALEM PALING OP NGENTOT**")


# Create by myself @skyzuex


CMD_HELP.update(
    {
        "gabut": "**Modules** - `Gabut`\
        \n\n Cmd : `.l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `.perkenalkan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `.jelek`\
        \nUsage : ngeledek orang yang jelek\
        \n\n Cmd : `.g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `.kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `.kalem`\
        \nUsage : kalem pokonya\
        \n\n Cmd : `.p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
