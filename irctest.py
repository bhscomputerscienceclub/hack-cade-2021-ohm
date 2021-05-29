import miniirc_extras
import miniirc
import random
import time


irc = None
code = ""
handle = None


def init(codee: int = None):
    nick = str(random.randint(100000, 100000000))
    if codee == None:
        codee = "#" + str(random.randint(1000000, 100000000))
    else:
        codee = "#" + str(codee)
    global code, irc
    code = codee
    irc = miniirc.IRC("10.13.13.2", 6667, nick, [code], auto_connect=False)
    irc.require("users")
    irc.connect()
    return irc


def twoppl() -> bool:
    return len(irc.users._users) == 2


def send(i: int):
    irc.msg(code, str(i))

def handle(handler):
    global handle
    handle = handler

if __name__ == "__main__":
    init(123)
    while not twoppl():
        time.sleep(0.1)
    handle(lambda x: print(x))
    print("other person joined")


@miniirc.Handler("PRIVMSG", colon=False)
def handler(irc: miniirc.IRC, hostmask: tuple, args):
    handle(int(args[1]))