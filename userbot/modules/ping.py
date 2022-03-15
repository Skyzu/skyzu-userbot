# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

import redis
from speedtest import Speedtest

from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS, StartTime
from userbot.events import register
from userbot.utils import edit_or_reply, skyzu_cmd

absen = [
    "**Eh ada skyzu**",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak** 😉",
    "**Hadir bang sky** 😁",
    "**Hadir kak maap telat** 🥺",
]

roas = [
    "DUH GINI NIH BOCAH YG LAHIR DI GUBUK BAMBU REOT + GAPUNYA HARGA DIRI, PADAHAL MAH DARI KECIL DIAJARIN SM EMAKNYA GABOLEH SONGONG SM MAJIKAN MASIH AJA SONGONG, MENDING LO URUSIN DULU GOBLOK KELUARGA LO YG PENYAKITAN ITU, MANA BAPA LO KAKINYA BOROK BEGITU AJG BERNANAH BAU AMIS IDIH GELI BET GELI GUA LIATNYA, NAH SEKALIAN TUH URUSIN JUGA ADE LO TUH, KALO BUKAN KARENA GUA MAH ADE LO UDAH MENINGGAL KENA TUMOR TOLOL MAKANYA LO KUDU SUJUD DEPAN GUA YAKAN,EMAK LO JUGA TUH JAGAIN UDAH BISU BEGITU YAKAN TAKUTNYA JATOH GABISA TREAK, MAKANYA NIH YA JANGAN KEBANYAKAN KONSUMSI SASA MICIN GOBLOK LIAT KAN EFEKNYA LO JADI KEK BOCAH AYAN BEGITU, SAMPE² LO BERANI GITU YAKAN NYENGGET JEMURAN ORANG SAMPE LO DIPUKULIN TRUS DI INJEK² SAMA WARGA SEKAMPUNGAN, GINI YA GUA KASIH TAU NIH SAMA LO NIH KALO UDA MISKIN KAGA USAH BELAGU SEGALA TOLOL, MIKIR LO MAKAN AJA SUSAH SAMPE NGEMIS² DI KOMPLEK PERUMAHAN GUA SAMPE DI USIR SAMA SATPAM KOMPLEK GUA, BERAS AJA LO BOLEH DIBAGI SAMA EMAK GUA YAKAN LAUK PAUK IKAN, AYAM, DAGING SEGALA RUPA AJA LO BOLEH NYOLONG DARI PASAR BOCAH KAYA LO MAH GIZINYA KURANG DONGO SABAN HARI MAKAN INDOMI 1 PAKE TELOR DOANG ITU JUGA JOINAN SM KELUARGA LU, KARENA APA?, YA KARENA LO MISKIN GA MAMPU BELI MAKANAN YG BERGIZI, DIKASIH KUAH SAYUR KANGKUNG JUGA MAO TOLOL ITU JUGA UDAH BERSYUKUR BISA MAKAN MAKANAN SELAEN MI INSTAN YAKAN SECARA LO GABISA GITU KEK GUA YAKAN MAKAN APA YG GUA MAO LAH ELO MAKAN MAKANAN TONG SAMPAH JUGA UDAH ALHAMDULILLAH BANGET AJG",
    "BUAT LO KONTOL NIH KALO UDAH HINA GAUSAH SOK SOK NGEHINA HINA GUA KONTOL, GUA TERLALU SUCI BUAT LU YANG HINA ITU ADUHHH. SINI GUA LUDAHIN DLU LU BIAR DIRI LU SUCI KARENA LU TAU LUDAH GUA ITU MULIA SEKALI",
    "PUNYA EMAK JANGAN JELEK GUE TAU EMAK LO UDAH MUKA JELEK ITEM BAT ITEM KEK OLI MOTOR BELOM DI GANTI SETAHUN HAHA TERUS BADANNYA GENDUT BAT GENDUT TETENYA KONDOR LAGI PANTESAN AJA KAGA LAKU HAHAHA NIH GUA KASIH TAU YE SAMA LO BOKAP LO AJE KERJAANNYA MAEN JUDI MULU BORO BORO MENANG BOKAP LO AJE MAEN JUDI KALAH MULU TOLOL HAHA UDAH NGUTANG SANA SINI AMPE DI KEJAR DEB COLLECTOR ITU BOKAP LO LAGI DI BURU OLEH DEP COLECTOR MANGKANYA KALO UDAH TAU MISKIN KERJAANNYA JANGAN MAEN JUDI MULU TOLOL SAMA NGUTANG CARI KERJA YANG HALAL SONO HAHA",
    "EHH TOLOL PEKERJAAN KAKEK LO DULU ITU JADI BABU BABU KOMPENI YANG DI SURUH BIKININ KOPI TERUS MOTONG RUMPUT DI HALAMAN RUMAH YAELAH KASIAN BAT KASIAN KAKEK LO ITU UDAH KONTET KURUS KERING KEREMPENG LAGI KAKEK LO DULU MATINYA KE ABISAN TENAGA PAS NYABUTIN RUMPUT TOLOL HAHA NENEK LO JUGA JADI LACUR KOMPENI NENEK LO AJE JADI LACUR KOMPENI CUMA DI BAYAR PAKE SINGKONG REBUS DOANG SATU BIJI TERUS NENEK LO ITU MATINYA PAS DI GANGBANG SAMA TENTARA KOMPENI MEMEK NENEK LO ITU DI SODOK SODOK MAKE SENAPAN NOH SAMPE MEMEKNYA LOBEH LEBAR BAT LEBAR KEK JALAN RAYA HAHA.BADUR BADUT IYE GUE TAU LO MAIN TELE ITU DI JADIIN BADUT ALIANSI KAN HAHAHA MANGKANYA BANG KALO JADI ORANG PAS DI SENGGOL LAWAN JANGAN DIEM BAE KEK BATU HAHA DI JADIIN BADUT KAN LO DI LEDEK LEDEKIN SAMA SEMUA ALIANSI,GUE TAU TUJUAN LO MAEN TELE ITU UNTUK MENCARI MEMEK MEMEK SEGAR KAN HAHA KETAUAN ORANG ORANG KEK LO OTAK SANGEAN YANG HAUS AKAN MEMEK DAN TOKET SAKING GK MAU MODAL DI RL BUAT NYEWA LACUR JADI LO MEMILIH BIAT MAIN TELE BORO BORO DAPET LAH LU KAGA DAPET SAMA SEKALI MANGKANYA GANTENG KONTOL LO UDAH JELEK PENGENNYA YANG BAGUS BAGUS NYADAR DIRI LO ITU UDAH JELEK TERUS MISKIN LAGI",
    "MAS KALO UDA NGANTUK BOBO AJA JANGAN MAKSAIN TERUS BUAT LAWAN GUA TAKUTNYA LO BESOK KENA ANGIN DUDUK DOANG TERUS MATI DAH KAN KASIAN UDAH JADI BEBAN KELUARGA MALAH NAMBAHIN BEBAN TOLOL. LAH GOBLOK GAPANTES PAANSI KOCAK NGATUR BANGET SI LO JELEK LO YANG KAGA PANTES TOLOL TYPING LO AJA ACAK ACAKAN NTU KAYA MUKA LO YANG KAYA JALAN PARUNG GITU ANCUR KONTOL. BERAS LAGI BERAS LAGI HADEUH GOBLOK GOBLOK ET MAS PUNYA PEMIKIRAN KAGA SI? ET IYA LUPA OTAK BE ORA ADA APALAGI PEMIKIRAN YA WKWK GOBLOK. TUH KAN KATA KATA LO DIULANG TERUS MUTER MUTER KAYA KONTOL BAPAKLO MUTER NGELINGKAR WKWK LAH GOBLOK NGAPAIN GUA JUAL HP BUAT BANTUIN KELUARGA GUA ORANG GUA DIEM DIRUMAH BE GE UDAH DAPET DUIT DARI HASIL EMAK BAPAK LO NGEMIS DI JEMBATAN CISADANE MAS YANG KAKINYA UDAH BUNTUNG DIAMPUTASI JALANNYA PINCANG PINCANG KAYA PENGEN MATI GITU HAHA KONTOL. TUH EPEP TERUS LO MA AH MENDING LO BOBO SONO KALO KAGA LO NANGIS DIPOJOKAN SEBARI MAININ TITIT ABIS ITU LO NGADU KE BAPAK LO KALO LO DIHINA HINA TERUS SM GUA SAMPE KENA MENTAL TERUS STRESS DAH LO KAYA SEKARANG WKWK NGENTOT",
    "TOLOL BAT SIH ANJG LU TYPING SOBAT KEREN BEGITU MANA TYPNG KOSA KATA BASI BAT BASI KEK MEMEK MAKLU YANG UDAH BASI KESERINGAN DIEWE AMA BAPAK BAPAK KOMPLEK DIGILIR DIMASUKIN PIPA PARALON KALO GAK BAMBU UDAH LEBAR KEK GUA BEGITU CUIH KAGA USAH SOBAT KEREN TOLOL MAKLU NOH DI LUAR NEGERI CUMA JADI KACUNG YANG KERJAANNYA CUMA BERSIH BERSIH DAN MALAH KERJANYA KAGA PERNAH BENER EH MAKLU DENGAN SIFAT BINALNYA NGEGODA MAJIKAN BIAR DIEWE BIAR TAMBAH GAJI BUKANNYA GAJINYA NAMBAH MALAH MAKLU NOH DIPECAT KARENA KETAUAN UDAH BUNTING EH PULANG PULANG BAPAK LU LIAT NYA LANGSUNG JANTUNGAN KENA STROKE KARENA BAPAK LU KENA PENYAKIT KOMPLIKASI YAELAH NAJIS CUIH BAPAK LU HIDUP NYA CUMA REBAHAN SABAN HARI BOKER KENCING MAKAN DIKASUR MANA DICEBOKIN MAKE AIR LIUR KARENA SAKING MISKIN NYA KELUARGA LU AIR AJA KAGA MAMPU TOLOL SADAR DIRI BEGO KELUARGA LU AJA UDAH DIUSIR SAMA WARGA KARENA BAU BAPAK LU UDAH KAGA JELAS NGERACUNIN WARGA MENDING LU BALIK NOH KE HUTAN YE LU BIKIN RUMAH DARI RANTING KAYU ATAP PAKE ALANG ALANG ALAS TIDUR MAKE DAUN PISANG KAGA USAH SOK IYE KALO BAPAK LU AJA BENTAR LAGI MATI KAGA ADA YANG MAU NGUBUR JUGA KARENA PENYAKIT NYA BERBAHAYA DAN JALAN SALAH SATUNYA DIBAKAR DAN MAKLU NGEMIS KERUMAH GUA BIAR DAPET DUIT BUAT BELI BENSIN NAJIS CUIH YE MAKLU NOH DILAMPUERAH OPEN BO BUKANNYA DAPET DUIT MALAH DIGANG BANG ANAK PUNK CUMA DIBAYAR DIAJAKIN MABOK DICIU RAME RAME NAJIS BAT SIH KELUARGA LU TOLOL YE MENDING NIH LU JAN JADI BEBAN KELUARGA TOLOL SADAR DIRI BEGO ADEKLU CUMA BUAT JAJAN AJA AMPE NYEPONGIN KONTOL TETANGGA YAILAH NAJIS CUIH KAGA KEREN KERENNYA KELUARGA LU BEGO YE LU TU ANAK HARAM HASIL GANGBANGAN SUPIR ANGKUTAN YANG HABIS LAHIR DIBUANG KEHUTAN DIASUH AMA MONYET BEKANTAN MANA HIDUP NYA GELANTUNGAN UDAH KEK TARZAN KAGAK TAU ATURAN MUKALU AJA BERANTAKAN MAKANYA NIH MANDI TOLOL HIDUP JAN CUMA NGOTORIN BUMI DOANG YE MENTANG MENTANG DIHUTAN SUSAH AIR MANDI CUMA NUNGGU AIR HUJAN MANA KAGA MAKE SABUN MAKENYA CUMA BATU BUAT GOSOKAN ITUPUN KAGA NGELUNTURIN DAKI LU YANG UDAH 5 CM TEBEL NYA YAILAH MANA MAKE DAUN DAUN DOANG BIAR AGAK WANGIAN MUKA LU NOH UDAH GRADAGAN BOLONG BOLONG KEK JALAN PEDESAAN MANA BERMINYAK UDAH KEK SPONS CUCI PIRING MANA BAPAK LU KIKIR BAT KEK TUAN KEK IDUNG LU UDAH GEDE KEK SQUIDWARD KARENA PENYAKIT POLIP EH KONTOL UDAH KECIL KEK PLANTOK MANA LEBIH KECIL LAGI UDAH KEK CACING PITA NAJIS CUIH MANA CUMA JADI PARASIT DOANG IDUP LU NAJIS",
    "EH TOLOL LU LAGI NGATAIN DIRI SENDIRI YEH WKWKWK KASIAN BATT KASIAN BARU LIAT MUKA LU AJA UDAH KETEBAK KALAU LU TUH JABLAY TELE YANG HOBBY NYA TUH SUKA OMEK² DEPAN UMUM WKWK YANG KALAU DI BAYAR PAKE DUIT RECEHAN JUGA MASIH TTP DI GAS YAHHH KETAHUAN KAN MAKANYA KALAU MAU NGATAIN ORANG TUH NGACA DLU BHAAKKS EHH LUPA LU KAN KGK PUNYA KACA TOLOL ORANG MISKIN YANG BERLAGAK ORANG KAYA MANA PUNYA KACA WKWK",
    "WKWKWK BABU BABU TONGKRONGAN KAYA LAU BELOM CUKUP BUAT NGENAIN INI CLAN TOLOL, APALAGI DISINI ADA GW, BABY NIH BOS GA PAKE TITTLE GA BAWA CLAN GA BAWA ALIANSI GOSAH BANYAK TINGKAH KALO WAR TYPING AMA GW MASIH TREMOR JIWA LU JIWA KACUNG JADI GOSAH BERLAGAK SEOLAH LU MAJIKAN BAHAHAHAHAHAHAH GINI NIH KALO JAMET FB NYASAR KETELE MENDING LU MAEN HAGO BEGO PELIHARA DOMBA LUMAYAN DIJUAL BISA BUAT MAKAN SEHARI HARI GOSAH NYUSAHIN GW, KAGA ADA GW LU GA MAKAN TOLOL DIKASIH SANTUNAN BUAT NYAMBUNG IDUP EH MALAH MASANG TOGEL MAEN CEWE SONO SINI KENA PENYAKIT MANA NYOKANYA DISURUH JADI LACUR MAEN BIGO LIVE KEMAREN GW SAWER 2RIBU NGANGKANG NGANGKANG SAMBIL PASANG MUKA SANGE YANG GA COCOK BANGET DI MUKA NYOKAPLU TOLOL, BAPAK LU MALU LIAT KELAKUANLU KE GITU OIYA SORRY LU NAK YATIM YANG GA PUNYA BOKAP BAHAHAHAHAHAHAH JADI INGET",
    "GUA MASIH MENDING BELAJAR TOLOL DARI PADA LO GA PERNAH BELAJAR AHAHA MAKANYA LO ITU MISKIN PENDIDIKAN MISKIN HARTA AHAHA MISKIN EKONOMI SERBA MISKIN KELUARGA LO ANJING AHAHA KOCAK BANGET TOLOL LO ITU PANTES NYA JADI BADUT MAMPANG KALO GA BADUT ANCOL YANG PALANYA GEDE SAMA IDUNH NYA LONJONG UDAH KAYA TIMUN SURI AHAHA JELEK KALO UDAH TUA RETAK DAH TUH SAMA KAYA MUKA LO YA RETAK JAJAR GENJANG DAN TRAPESIUM AHAHAH MENYE BAT MENYEE MAKANYA KALO PUNYA MUKA YANG KERENAN DIKIT LO KAN LAHIR SIA SIA TUHAN JUGA GA NGANGGEP LO HAMBANYA AHAHA KARENA TUHAN LO GHOIB DAN KO JUGA NYEMBAH BATU",
    "WKWK KOCAH LO MENDING JADI SUPER MARIO AJA NOH BILANG KE KAKE NENEK LO MENDING JADI SUPER MARIO KALO GA LOST SAGA HAHA JADI BOCAH POINT BLANK DIA BOLOT ANJING AHAHA MAKANYA KALO PUNYA KUPING YANG BENERAN DIKIT TOLOL KUPING LO CONGE NYA BLEBERAN SAMPE LUAR LUAR KALI YA AHAHA KASIHAN BANGET GUA LIAT LO BERPENYAKITAN SEGALA MACEM ADA WKWK DAN BURUK NYA LO TUH LO UDAH KAYA LEAK GITU UDAH ITU MULUT UDAH KAYA JULUNG JULUNG GITU JELEK BANGET KAYA NUGET GITU YA MUKA LO BIBIR LO SUMBING YA APA DOBLEH AHAHAH",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=DEVS, pattern=r"^.absen$")
async def _(skyzuu):
    await skyzuu.reply(random.choice(absen))


@register(incoming=True, from_users=2122770443, pattern=r"^.roas$")
async def _(skyzuu):
    await skyzuu.reply(random.choice(roas))


@skyzu_cmd(pattern="sping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**🐖 ADA BABI🐖 **")
    await pong.edit("**🐖🐖 ADA BABI 🐖🐖**")
    await pong.edit("**🐖🐖🐖 ADA BABI 🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖 LU BABI 🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖 OINKK 🐖🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖🐖 OINKK 🐖🐖🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖🐖🐖 OINKK 🐖🐖🐖🐖🐖🐖🐖**")
    await pong.edit("`.................🐖`")
    await pong.edit("`................🐖.`")
    await pong.edit("`...............🐖..`")
    await pong.edit("`..............🐖...`")
    await pong.edit("`.............🐖....`")
    await pong.edit("`............🐖.....`")
    await pong.edit("`...........🐖......`")
    await pong.edit("`..........🐖.......`")
    await pong.edit("`.........🐖........`")
    await pong.edit("`........🐖.........`")
    await pong.edit("`.......🐖..........`")
    await pong.edit("`......🐖...........`")
    await pong.edit("`.....🐖............`")
    await pong.edit("`....🐖.............`")
    await pong.edit("`...🐖..............`")
    await pong.edit("`..🐖...............`")
    await pong.edit("`.🐖................`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**{ALIVE_NAME}**        \n"
        f"**➾Kecepatan : ** %sms  \n"
        f"**➾Branch : ** Skyzu-Userbot \n" % (duration)
    )


@skyzu_cmd(pattern="lping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Connecting...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**`{ALIVE_NAME}`**\n"
        f"✧ **-ꜱɪɢɴᴀʟ- :** "
        f"`%sms` \n"
        f"✧ **-ᴜᴘᴛɪᴍᴇ- :** "
        f"`{uptime}` \n" % (duration)
    )


@skyzu_cmd(pattern="xping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**⚡𝐒𝐊𝐘𝐙𝐔 𝐔𝐒𝐄𝐑𝐁𝐎𝐓​⚡**\n"
        f"➾ __Signal__    __:__ "
        f"`%sms` \n"
        f"➾ __Uptime__ __:__ "
        f"`{uptime}` \n" % (duration)
    )


@skyzu_cmd(pattern="sinyal$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    sky = await edit_or_reply(ping, "**mengecek sinyal...**")
    await sky.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await sky.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await sky.edit("**40% ████▒▒▒▒▒▒**")
    await sky.edit("**60% ██████▒▒▒▒**")
    await sky.edit("**80% ████████▒▒**")
    await sky.edit("**100% ██████████**")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await sky.edit(
        f"**⚡𝐒𝐊𝐘𝐙𝐔 𝐔𝐒𝐄𝐑𝐁𝐎𝐓​⚡**\n"
        f"** ▹  Sɪɢɴᴀʟ   :** "
        f"`%sms` \n"
        f"** ▹  Uᴘᴛɪᴍᴇ  :** "
        f"`{uptime}` \n"
        f"** ▹  Oᴡɴᴇʀ   :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@skyzu_cmd(pattern="ping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    sky = await edit_or_reply(ping, "**𖣘**")
    await sky.edit("**𖣘𖣘**")
    await sky.edit("**𖣘𖣘𖣘**")
    await sky.edit("**◕‿- PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await sky.edit(
        f"**PONG!!🏓**\n"
        f"• **Pinger** - "
        f"`%sms` \n"
        f"• **Uptime** - "
        f"`{uptime}` \n"
        f"**✦҈͜͡➳ Owner:** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@skyzu_cmd(pattern="kecepatan$")
async def speedtst(spd):
    """For .speed command, use SpeedTest to check server speeds."""
    await spd.edit("**Sedang Menjalankan Tes Kecepatan Jaringan,Mohon Tunggu...**")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit(
        "**Kecepatan Jaringan:\n**"
        " ━━━━━━━━━━━━━━━━━ \n"
        f"✧ **Dimulai Pada :**  \n"
        f"`{result['timestamp']}` \n"
        "✧ **Download:** "
        f"`{speed_convert(result['download'])}` \n"
        "✧ **Upload:** "
        f"`{speed_convert(result['upload'])}` \n"
        "✧ **Signal:** "
        f"`{result['ping']}` \n"
        "✧ **ISP:** "
        f"`{result['client']['isp']}` \n"
        "✧ **BOT:** ⚡skyzu-userbot⚡"
    )


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@skyzu_cmd(pattern="pong$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    await pong.edit("`Pong...........🐤`")
    await pong.edit("`Pong..........🐤.`")
    await pong.edit("`Pong.........🐤..`")
    await pong.edit("`Pong........🐤...`")
    await pong.edit("`Pong.......🐤....`")
    await pong.edit("`Pong......🐤.....`")
    await pong.edit("`Pong.....🐤......`")
    await pong.edit("`Pong....🐤.......`")
    await pong.edit("`Pong...🐤........`")
    await pong.edit("`Pong..🐤.........`")
    await pong.edit("`Pong.🐤..........`")
    await pong.edit("`Pong🐤...........`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**⚡Oᴡɴᴇʀ : {ALIVE_NAME}**\n📗 `%sms`" % (duration))


@skyzu_cmd(pattern="pink$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8===✊D💦")
    await pong.edit("8====D💦💦")
    await pong.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**KONTOL!! **\n**NGENTOT** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@skyzu_cmd(pattern="fping$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    datetime.now()
    await pong.edit(".                       /¯ )")
    await pong.edit(".                       /¯ )\n                      /¯  /")
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /"
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸"
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ "
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')"
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /"
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´"
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              ("
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  "
    )


CMD_HELP.update(
    {
        "ping": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ping` | `{cmd}lping` | `{cmd}xping` | `{cmd}sinyal` | `{cmd}sping` | `{cmd}pink` | `{cmd}fping`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}kecepatan`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}pong`\
         \n↳ : Sama Seperti Perintah Ping."
    }
)
