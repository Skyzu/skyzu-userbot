from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ASSALAMUALAIKUK ANAK NGENTOT")


@register(outgoing=True, pattern="^K(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("SA AE LU JELEK")


@register(outgoing=True, pattern="^L(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("WAALAIKUMSALAM GOBLOK")


@register(outgoing=True, pattern="^D(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**DAR DER DOR DAR DER DOR PELER BAPA KAU GUA GEDOR SINI NGENTOT!!**"
    )


@register(outgoing=True, pattern="^M(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU KAYA MONYET**")


@register(outgoing=True, pattern="^N(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BIBIR LU DOER NGENTOT**")


@register(outgoing=True, pattern="^H(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSA KETAWA NGENTOT GIGI LU KUNING**")


@register(outgoing=True, pattern="^B(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA JERAWATAN GITU ANJING**")


@register(outgoing=True, pattern="^Y(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**MAKAN ULAT SAGU DIPINGGIR JALAN TOL, GAUSAH BELAGU YA KONTOL**"
    )


@register(outgoing=True, pattern="^C(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ANAK YATIM MUKA KAYA LUTUNG, JANGAN SO IYE LU BUNTUNG**")


@register(outgoing=True, pattern="^S(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SEKUTU KONTOOOLLL**")


@register(outgoing=True, pattern="^V(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GC AMPAS NGENTOT**")


@register(outgoing=True, pattern="^J(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GUA KEREN GA KAYA LU KONTOL JELEK**")


@register(outgoing=True, pattern="^A(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BISMILLAH NGEWE SAMA KAMU, AHT AHT**")


@register(outgoing=True, pattern="^X(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SEKUTU AMPAS BET NGENTOT**")


@register(outgoing=True, pattern="^Z(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**WAR WAR TAI ANJING, KOSA KATA LU AJA GITU GITU DOANG NGENTOT MENDING LU PULANG AJA BEGO GAPANTES LU MAIN TELEGRAM, BANTUIN EMAK LU COLMEK AJA KONTOL**"
    )


@register(outgoing=True, pattern="^KEREN(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GUA KERENN MAKASI**")


@register(outgoing=True, pattern="^O(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MAIN BOT MULU LU NGENTOT, NANTI BOT RUSAK MINTA BENERIN LU KONTOL**")


@register(outgoing=True, pattern="^G(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SO KEREN LU BUKAN JOO**")


CMD_HELP.update(
    {
        "salam": "P\
\nUsage: Untuk Memberi salam.\
\n\nL\
\nUsage: Untuk Menjawab Salam.\
\n\nK\
\nUsage: Memperkenalkan Diri.\
\n\nN\
\nUsage: Menanyakan Kabar.\
\n\nB\
\nUsage: Sok Kepinteran.\
\n\nM\
\nUsage: Ngajak Ngopi!!.\
\n\nY\
\nUsage: Gc Nya Kaya kuburan.\
\n\nC\
\nUsage: Dia tuh Ngeyel banget.\
\n\nS\
\nUsage: Haha sokap."
    }
)

CMD_HELP.update(
    {
        "salam2": "V\
\nUsage: Merendah.\
\n\nJ\
\nUsage: Nyari Sleep Call.\
\n\nA\
\nUsage: Hujat yang gapunya muka.\
\n\nX\
\nUsage: Kegantengan.\
\n\nZ\
\nUsage: teruntuk petarung.\
\n\nH\
\nUsage: Kecantikan.\
\n\n.atg\
\nUsage: Istighfar.\
\n\n.dor\
\nUsage: gatau.\
\n\nO\
\nUsage: Ngatain org norak.\
\n\nG\
\nUsage: Liat Sendiri."
    }
)
