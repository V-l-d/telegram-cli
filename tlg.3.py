# -*- coding: utf-8 -*-

"""
tg
git clone --recursive https://github.com/vysheng/tg.git && cd tg
sudo apt-get update
sudo apt-get install libreadline-dev libconfig-dev libssl-dev lua5.2 liblua5.2-dev libevent-dev libjansson-dev libpython-dev make 
./configure
make
bin/telegram-cli -k tg-server.pub
bin/telegram-cli -k <public-server-key>
msg @user 'text'

tytg
https://github.com/luckydonald/pytg
sudo pip install pytg
sudo pip install --upgrade pytg

from pytg.sender import Sender
help(Sender)  # list all commands
help(Sender.get_self)  # get help for a specific command

sender.send_msg('@user', 'text')

GitHub
echo "# telegram-cli" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/V-l-d/telegram-cli.git
git push -u origin master


"""

from pytg import Telegram
from pytg.utils import coroutine
import time
from pytg.utils import coroutine

# USER_NAME = 'V_ladimir'
USER_NAME = 'dmytryistriletskyi'
BOT_NAME = 'ya'

tg = Telegram(
    telegram="/home/ubuntu/workspace/tg/bin/telegram-cli",
    pubkey_file="/home/ubuntu/workspace/tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender


@coroutine     # from pytg.utils import coroutine
def main_loop():
    """ Ждем ответа """
    QUIT = None
    while not QUIT:
        print('----------------')
        msg = (yield)     # it waits until it got a message, stored now in msg.
        try:
            user = msg.sender.username
            message = msg.text
            print(msg)
            print(user, message)
            if user == USER_NAME:
                sender.send_msg('@{user}'.format(user = BOT_NAME), message)
            elif user == BOT_NAME:
                sender.send_msg('@{user}'.format(user = USER_NAME), message)
        except AttributeError:
            print('pass')
        QUIT = False

# start the Receiver, so we can get messages!
receiver.start()

# let "main_loop" get new message events.
# You can supply arguments here, like main_loop(foo, bar).
# receiver.message(main_loop())
# now it will call the main_loop function and yield the new messages.


sender.send_msg('@{user}'.format(user = USER_NAME), 'Привет!')
receiver.message(main_loop())
