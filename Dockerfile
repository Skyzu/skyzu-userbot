# Using Python Slim-Buster
FROM mrismanaziz/man-userbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Skyzuu-Userbot ━━━━━

RUN git clone -b Skyzuu-Userbot https://github.com/Skyzu/skyzu-userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r requirements.txt

# Finalization
CMD ["python3", "-m", "userbot"]
