from platform import uname

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.events import register
from userbot.utils import skyzu_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐬𝐬𝐚𝐥𝐚𝐦𝐮'𝐚𝐥𝐚𝐢𝐤𝐮𝐦...")


@skyzu_cmd(pattern="atg(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇....SAYANG!!!!")


@register(outgoing=True, pattern="^L(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐖𝐚'𝐚𝐥𝐚𝐢𝐤𝐮𝐦𝐬𝐚𝐥𝐚𝐦...")


@skyzu_cmd(pattern="dor(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**DAR DER DOR DAR DER DOR PALA BAPA KAU GW GEDOR SINI NGENTOT!!**"
    )


@register(outgoing=True, pattern="^K(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOLLU ITEM GAUSAH SOK NGAJAKIN VCS GOBLOK!!**")


@register(outgoing=True, pattern="^N(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**𝐍𝐆𝐄𝐍𝐓𝐎𝐓𝐓𝐓𝐓**")


@register(outgoing=True, pattern="^B(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BHAHAHAHAHAHAHA**")


@register(outgoing=True, pattern="^M(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MASIH KECIL GAUSAH BLAGU LU NGENTOT!!**")


@register(outgoing=True, pattern="^Y(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**MAKAN ULAT SAGU DIPINGGIR JALAN TOL, LO PADA GAUSAH BELAGU YA KONTOL**"
    )


@register(outgoing=True, pattern="^C(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KAN UDAH GUA BILANG??MAKANYA JANGAN NGEYEL GOBLOK!!**")


@register(outgoing=True, pattern="^S(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOKAP DEH KAMU!!**")


@register(outgoing=True, pattern="^V(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MACAM BAGUS AE LU BEGITU SETDAH!!**")


@register(outgoing=True, pattern="^J(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MAAF BUKAN JAGOAN HAHAHAHA!!**")


@register(outgoing=True, pattern="^A(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BISMILLAH SLEEP CALL!!😁**")


@register(outgoing=True, pattern="^X(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GANTENG LU BEGITU???**")


@register(outgoing=True, pattern="^Z(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**War War Tai anjing, Ketrigger minta sharelok, Udah di sharelok Ga nyamperin,Keras di sosmed Bhakss...**"
    )


@register(outgoing=True, pattern="^H(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CANTIK LU BEGITU???**")


@register(outgoing=True, pattern="^O(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MAIN BOT MULU LU NGENTOT, KESANNYA NORAK GOBLOK!!**")


@register(outgoing=True, pattern="^G(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GA KEREN LU BEGITU NGENTOT!**")


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
        "salam2": f"V\
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
\n\n{cmd}atg\
\nUsage: Istighfar.\
\n\n{cmd}dor\
\nUsage: gatau.\
\n\nO\
\nUsage: Ngatain org norak.\
\n\nG\
\nUsage: Liat Sendiri."
    }
)
