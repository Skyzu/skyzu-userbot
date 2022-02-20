from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import skyzu_cmd


@skyzu_cmd(pattern="sayang(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("**Cuma Mau Bilang**")
    sleep(3)
    await typew.edit("**Aku Sayang Kamu**")
    sleep(1)
    await typew.edit("**I LOVE YOU 💞**")


# Create by myself @localheart


@skyzu_cmd(pattern="semangat(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("**Apapun Yang Terjadi**")
    sleep(3)
    await typew.edit("**Tetaplah Bernapas**")
    sleep(1)
    await typew.edit("**Dan Selalu Bersyukur**")


# Create by myself @localheart


@skyzu_cmd(pattern="jamet(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WOII**")
    sleep(1.5)
    await typew.edit("**JAMET KONTOL**")
    sleep(1.5)
    await typew.edit("**CUMA MAU BILANG**")
    sleep(1.5)
    await typew.edit("**GAUSAH SO ASIK**")
    sleep(1.5)
    await typew.edit("**EMANG KENAL?**")
    sleep(1.5)
    await typew.edit("**GAUSAH REPLY**")
    sleep(1.5)
    await typew.edit("**KITA BUKAN KAWAN**")
    sleep(1.5)
    await typew.edit("**GASUKA PC ANJING**")
    sleep(1.5)
    await typew.edit("**BOCAH KAMPUNG**")
    sleep(1.5)
    await typew.edit("**MENTAL TEMPE**")
    sleep(1.5)
    await typew.edit("**LEMBEK NGENTOT🔥**")


@skyzu_cmd(pattern="pp(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**PASANG PP DULU NGENTOT,BIAR ORANG-ORANG TAU BETAPA HINA NYA MUKA LU**"
    )


@skyzu_cmd(pattern="dp(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU HINA, GAUSAH SOK KERAS YA NGENTOT!!**")


@skyzu_cmd(pattern="so(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOKAB SAMA GUA NGENTOT, LU BABU GA LEVEL!!**")


@skyzu_cmd(pattern="met(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA BHAHAHA**")


@skyzu_cmd(pattern="war(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN...**"
    )


@skyzu_cmd(pattern="wartai(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA TOLOL**"
    )


@skyzu_cmd(pattern="kismin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU NGENTOT!!**"
    )


@skyzu_cmd(pattern="ded(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI**")


@skyzu_cmd(pattern="sokab(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SOKAB BET SI LU NGENTOT!!**")


@skyzu_cmd(pattern="gembel(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS KONTOL!!**"
    )


@skyzu_cmd(pattern="cuih(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CIH GE KEREN LO BEGITU GOBLOK!!**")


@skyzu_cmd(pattern="dih(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU KONTOL!**"
    )


@skyzu_cmd(pattern="gcs(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!**")


CMD_HELP.update(
    {
        "war": f"**Plugin : **`war`\
        \n\n  •  **Syntax :** `{cmd}jamet`\
        \n  •  **Function : **Menghina Jamet telegram\
        \n\n  •  **Syntax :** `{cmd}pp`\
        \n  •  **Function : **Menghina Jamet telegram yang ga pake foto profil\
        \n\n  •  **Syntax :** `{cmd}dp`\
        \n  •  **Function : **Menghina Jamet muka hina!\
        \n\n  •  **Syntax :** `{cmd}so`\
        \n  •  **Function : **Ngeledek orang sokab\
        \n\n  •  **Syntax :** `{cmd}met`\
        \n  •  **Function : **Ngeledek si jamet caper\
        \n\n  •  **Syntax :** `{cmd}war`\
        \n  •  **Function : **Ngeledek orang so keras ngajak war\
        \n\n  •  **Syntax :** `{cmd}wartai`\
        \n  •  **Function : **Ngeledek orang so ketrigger ngajak cod minta sharelok\
        \n\n  •  **Syntax :** `{cmd}kismin`\
        \n  •  **Function : **Ngeledek orang kismin so jagoan di tele\
        \n\n  •  **Syntax :** `{cmd}ded`\
        \n  •  **Function : **Nyuruh orang mati aja goblok wkwk\
        \n\n  •  **Syntax :** `{cmd}sokab`\
        \n  •  **Function : **Ngeledek orang so kenal so dekat padahal kga kenal goblok\
        \n\n  •  **Syntax :** `{cmd}gembel`\
        \n  •  **Function : **Ngeledek bapaknya si jamet\
        \n\n  •  **Syntax :** `{cmd}cuih`\
        \n  •  **Function : **ngatain orang sok keren\
        \n\n  •  **Syntax :** `{cmd}dih`\
        \n  •  **Function : **Ngeledek anak haram\
        \n\n  •  **Syntax :** `{cmd}gcs`\
        \n  •  **Function : **Ngeledek gc sampah\
        \n\n**Klo mau Req, kosa kata dari lu Hubungi @skyzu**\
    "
    }
)
