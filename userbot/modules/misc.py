import asyncio
import io
import os
import re
import sys
import urllib
from os import execl
from random import randint
from time import sleep

import requests
from bs4 import BeautifulSoup
from PIL import Image

from userbot import ALIVE_NAME, BOTLOG, BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, UPSTREAM_REPO_URL, bot
from userbot.utils import skyzu_cmd, time_formatter

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
REPOLINK = (
    str(UPSTREAM_REPO_URL)
    if UPSTREAM_REPO_URL
    else "https://github.com/Askarbot/Skyzuu-Userbot"
)
# ============================================

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


@skyzu_cmd(pattern="random")
async def randomise(items):
    """For .random command, get a random item from the list of items."""
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            "`2 or more items are required! Check .help random for more info.`"
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit(
        "**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" + itemo[index] + "`"
    )


@skyzu_cmd(pattern="sleep ([0-9]+)$")
async def sleepybot(time):
    """For .sleep command, let the userbot snooze for a few second."""
    counter = int(time.pattern_match.group(1))
    await time.edit("`I am sulking and snoozing...`")
    if BOTLOG:
        str_counter = time_formatter(counter)
        await time.client.send_message(
            BOTLOG_CHATID,
            f"You put the bot to sleep for {str_counter}.",
        )
    sleep(counter)
    await time.edit("`OK, I'm awake now.`")


@skyzu_cmd(pattern="shutdown$")
async def killdabot(event):
    """For .shutdown command, shut the bot down."""
    await event.edit("**Mematikan Skyzu-Userbot....**")
    await asyncio.sleep(7)
    await event.delete()
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, "#SHUTDOWN \n" "`Userbot Telah Dimatikan`"
        )
    await bot.disconnect()


@skyzu_cmd(pattern="restart$")
async def killdabot(event):
    await event.edit("**Restarting Skyzu-Userbot...**")
    await asyncio.sleep(10)
    await event.delete()
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, "#RESTARTBOT \n" "`Userbot Telah Di Restart`"
        )
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)
    # Shut the existing one down
    exit()


@skyzu_cmd(pattern="readme$")
async def reedme(e):
    await e.edit(
        "Here's Something for You to Read :\n"
        "\n[⚡ Skyzu-UserBot Repo](https://github.com/Askarbot/Skyzuu-Userbot/blob/skyzu-userBot/README.md)"
        "\n[Setup Guide - Basic](https://telegra.ph/How-to-host-a-Telegram-Userbot-11-02)"
        "\n[Special - Note](https://telegra.ph/Special-Note-11-02)"
    )


@skyzu_cmd(pattern="repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(" ", 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@skyzu_cmd(pattern="repo$")
async def repo_is_here(wannasee):
    """For .repo command, just returns the repo URL."""
    await wannasee.edit(
        "**Usᴇʀʙᴏᴛ Tᴇʟᴇɢʀᴀᴍ**\n"
        "𝗥𝗲𝗽𝗼 🇮🇩\n"
        "╰⎆ [𝐒𝐊𝐘𝐙𝐔-𝐔𝐒𝐄𝐑𝐁𝐎𝐓​](https://github.com/Skyzu/skyzu-userbot)\n"
        "❏ **Oᴡɴᴇʀ​** ⎆ [Skyzu](t.me/skyzu)\n"
        "❏ **Sᴜᴘᴘᴏʀᴛ**​ ⎆ [groups](t.me/skyzusupport)\n"
    )


@skyzu_cmd(pattern="raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit("`Check the userbot log for the decoded message data !!`")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Here's the decoded message data !!`",
        )


@skyzu_cmd(pattern="reverse(?: |$)(\d*)")
async def okgoogle(img):
    """For .reverse command, Google search images and stickers."""
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")

    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await bot.download_media(message, photo)
    else:
        await img.edit("`Harap Reply Di Gambar...`")
        return

    if photo:
        await img.edit("`Processing...`")
        try:
            image = Image.open(photo)
        except OSError:
            await img.edit("`Gambar tidak di dukung`")
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {"encoded_image": (name, open(name, "rb")), "image_content": ""}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers["Location"]

        if response != 400:
            await img.edit(
                "`Image successfully uploaded to Google. Maybe.`"
                "\n`Parsing source now. Maybe.`"
            )
        else:
            await img.edit("`Google told me to fuck off.`")
            return

        os.remove(name)
        match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
        guess = match["best_guess"]
        imgspage = match["similar_images"]

        if guess and imgspage:
            await img.edit(f"[{guess}]({fetchUrl})\n\n`Looking for images...`")
        else:
            await img.edit("`Couldn't find anything for your uglyass.`")
            return

        if img.pattern_match.group(1):
            lim = img.pattern_match.group(1)
        else:
            lim = 3
        images = await scam(match, lim)
        yeet = []
        for i in images:
            k = requests.get(i)
            yeet.append(k.content)
        try:
            await img.client.send_file(
                entity=await img.client.get_input_entity(img.chat_id),
                file=yeet,
                reply_to=img,
            )
        except TypeError:
            pass
        await img.edit(
            f"[{guess}]({fetchUrl})\n\n[Visually similar images]({imgspage})"
        )


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""

    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")

    results = {"similar_images": "", "best_guess": ""}

    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
                similar_image.get("value")
            )
            results["similar_images"] = url
    except BaseException:
        pass

    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()

    return results


async def scam(results, lim):

    single = opener.open(results["similar_images"]).read()
    decoded = single.decode("utf-8")

    imglinks = []
    counter = 0

    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, decoded, re.I | re.M)

    for imglink in oboi:
        counter += 1
        if not counter >= int(lim):
            imglinks.append(imglink)
        else:
            break

    return imglinks


CMD_HELP.update(
    {
        "random": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}random <item1> <item2> ... <itemN>`\
    \n↳ : Get a random item from the list of items.",
        "sleep": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}sleep <seconds>`\
    \n↳ : Let yours snooze for a few seconds.",
        "shutdown": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.shutdown`\
    \n↳ : Shutdown bot",
        "repo": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}repo`\
    \n↳ : Github Repo of this bot",
        "readme": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙 `{cmd}readme`\
    \n↳ : Provide links to setup the userbot and it's modules.",
        "repeat": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}repeat <no> <text>`\
    \n↳ : Repeats the text for a number of times. Don't confuse this with spam tho.",
        "restart": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}restart`\
    \n↳ : Restarts the bot !!",
        "raw": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}raw`\
    \n↳ : Get detailed JSON-like formatted data about replied message.",
    }
)
