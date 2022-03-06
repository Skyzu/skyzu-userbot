# Using Python Slim-Buster
FROM kyyex/kyy-userbot:busterv2
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Skyzuu-Userbot ━━━━━

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
RUN git clone -b Skyzuu-Userbot https://github.com/Skyzu/skyzu-userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Skyzu/skyzu-userbot/Skyzuu-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
