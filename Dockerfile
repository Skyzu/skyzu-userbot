# Using Python Slim-Buster
FROM Askarbot/Skyzuu-Userbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Skyzuu-Userbot ━━━━━

RUN git clone -b Skyzuu-Userbot https://github.com/Askarbot/Skyzuu-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Askarbot/Skyzuu-Userbot/Skyzuu-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
