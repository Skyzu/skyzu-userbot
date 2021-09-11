from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^D(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOT NGENTOTTT!!BAPA LU SURUH RIBUT SAMA GUA**")


@register(outgoing=True, pattern='^E(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK USAH SOK KERAS GOBLOK!!KENCING MASIH BERDIRI AJA BELAGU**")


@register(outgoing=True, pattern='^F(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU SEMUA KAYA KONTOL HAHAHAHA!!**")


@register(outgoing=True, pattern='^I(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL MASIH BENGKOK AJA BANGGA LU HAHAHAHA!!**")


@register(outgoing=True, pattern='^Q(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EHH GOBLOK LU SEMUA RIBUT SAMA GUA GOBLOK!!**")


@register(outgoing=True, pattern='^R(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL KONTOL APA YANG BESAR?KONTOL LU LAH HAHAHAHA!!**")


@register(outgoing=True, pattern='^T(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BABI!!KONTOL!!NGENTOT!!!**")


@register(outgoing=True, pattern='^U(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BABI LU GOBLOK!!GANTENGAN JUGA GUA HAHAHAHA**")


@register(outgoing=True, pattern='^W(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BABI LU GOBLOK!!CANTIKAN JUGA GUA HAHAHAHA**")


@register(outgoing=True, pattern='^Q(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOTAN LU GAK BIKIN GUA TREMOR GOBLOK HAHAHAHA!!**")

CMD_HELP.update({
    "toxic":
    "D\
\nUsage: Bacotin Orang.\
\n\nE\
\nUsage: Buat Orang Yang Sok Keras.\
\n\nF\
\nUsage: Ngatain Orang Wkwkkw.\
\n\nI\
\nUsage: Kontol Orang Ngatain.\
\n\nQ\
\nUsage: Ngajak Ribut Orang.\
\n\nR\
\nUsage: Pantun Anjing.\
\n\nT\
\nUsage: Nyebutin Binatang.\
\n\nU\
\nUsage: Biar Dikata Ganteng.\
\n\nW\
\nUsage: Biar Dikata Cantik.\
\n\nQ\
\nUsage: Tremor Kan Lu."
})
