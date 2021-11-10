# Using Python Slim-Buster
FROM vckyouuu/geezprojects:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Skyzuu-Userbot ━━━━━

RUN git clone -b Skyzuu-Userbot https://github.com/LevinSkuy/skyzu-userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/LevinSkuy/skyzu-userbot/skyzu-userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
