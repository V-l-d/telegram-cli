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

"""

from pytg import Telegram
from pytg.utils import coroutine
import time
from pytg.utils import coroutine

tg = Telegram(
    telegram="/home/ubuntu/workspace/tg/bin/telegram-cli",
    pubkey_file="/home/ubuntu/workspace/tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender

# Посылаем запрос пользователю
# sender.send_msg('@V_ladimir', 'Анегдот_777')
# sender.send_msg('@ya', 'Чем сегодян занят?')
#sender.send_msg('@{user}'.format(user = 'ya'), 'какой завтра праздник?')

# Ждем ответа
@coroutine     # from pytg.utils import coroutine
def main_loop():
    QUIT = None
    while not QUIT:
        msg = (yield)     # it waits until it got a message, stored now in msg.
        try:
            print(msg.sender.username)
            print(msg.text)
            if msg.sender.username == 'ya':
                print(msg)
                print(msg.text)
                print('@{user}'.format(user = 'V_ladimur'))
                sender.send_msg('@V_ladimir', msg.text)
                break
            else:
                sender.send_msg('@ya', msg.text)
        except AttributeError:
            print('pass')
            pass

        # do more stuff here!
        QUIT = False


# start the Receiver, so we can get messages!
receiver.start()

# let "main_loop" get new message events.
# You can supply arguments here, like main_loop(foo, bar).
receiver.message(main_loop())
# now it will call the main_loop function and yield the new messages.




