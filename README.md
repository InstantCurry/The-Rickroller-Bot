# The Rickroller
### A discord bot designed to annoy people
Written in python 3 with discord.py. Badly, since I kinda suck at python.

This will run on all major operating systems, but the installation instructions are for linux, because that's what I use.

#### Prerequisites

1. Git, nano, python 3.7+ and discord.py

  on Ubuntu:
```bash
    sudo apt install git nano -y
    pip3 install discord.py
```
2. Create a bot on Discord.com

  I'm not going to leave instructions here, just look at this: https://www.howtogeek.com/364225/how-to-make-your-own-discord-bot/

  Make note of your client ID

#### Installation:

1. Open up a terminal and clone this repository to your disk
```bash
    git clone https://github.com/InstantCurry/The-Rickroller-Bot.git
    cd The-Rickroller-Bot
```
2. Add your client ID from earlier.

    On line 43 of bot.py, paste your client ID into `client.run(CLIENTID HERE)`

3. In bash, run
```bash
    python3 bot.py
```
  if it complains about missing files, cd into the directory that you downloaded earlier, and try again

4. invite the bot to your server with scope "bot", and permissions "send messages".

  if you've got no idea what any of that means, just paste `https://discord.com/api/oauth2/authorize?client_id= {id here} &permissions=2048&scope=bot` into your web browser, where id here is your client ID from earlier.
