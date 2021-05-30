import miniirc_extras
import miniirc
import random
import time


irc = None
code = ""
actions: list[int] = [0]
prevsend = 0

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
    global prevsend
    if i != prevsend:
        irc.msg(code, str(i))
        prevsend = i


if __name__ == "__main__":
    init(123)
    while not twoppl():
        time.sleep(0.1)
    print("other person joined")
    while True:
        print(actions[-1])


@miniirc.Handler("PRIVMSG", colon=False)
def handler(irc: miniirc.IRC, hostmask: tuple, args):
    print("A")
    actions.append(int(args[1]))
