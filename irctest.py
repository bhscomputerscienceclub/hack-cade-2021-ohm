import miniirc_extras
import miniirc
import random
import time
from typing import List, Tuple

irc = None
code = ""
actions: List[int] = [0]
prevsend = 0
start_poss = None
fruit = None


def init(codee: int = None):
    nick = str(random.randint(100000, 100000000))
    if codee == None:
        codee = "#" + str(random.randint(1000000, 100000000))
    else:
        codee = "#" + str(codee)
    global code, irc
    code = codee
    irc = miniirc.IRC(
        "a.linode.servers.malhotra.cc", 29615, nick, [code], auto_connect=False
    )
    irc.require("users")
    irc.connect()
    return irc


def twoppl() -> bool:
    return len(irc.users._users) == 2


def senddir(i: int):
    global prevsend
    if i != prevsend:
        irc.msg(code, "dir " + str(i))
        prevsend = i


def start_pos() -> Tuple[int,int,int,int]:
    global start_poss
    if start_poss == None:
        irc.msg(code, "getstart")
    while start_poss is None:
        time.sleep(0.01)
    return tuple(start_poss[1:] + start_poss[:1])


def set_start_pos(a:int, b:int, c:int, d:int):
    print("HI")
    global start_poss
    start_poss = (a, b, c, d)


def send_start_pos():
    irc.msg(code, "start " + " ".join([str(i) for i in start_poss + fruit]))

def spawn_fruit():
    global fruit
    return fruit


if __name__ == "__main__":
    init(123)
    while not twoppl():
        time.sleep(0.1)
    print("other person joined")
    while True:
        print(actions[-1])


@miniirc.Handler("PRIVMSG", colon=False)
def handler(irc: miniirc.IRC, hostmask: tuple, args):
    global fruit, start_poss
    args = args[1].split(" ")
    if args[0] == "fruit":
        fruit = (int(args[1]), int(args[2]))
    elif args[0] == "getstart":
        send_start_pos()
    elif args[0] == "start":
        start_poss = tuple([int(args[i]) for i in (1, 2, 3, 4)])
        fruit = (int(args[5]), int(args[6]))
    elif args[0] == "dir":
        actions.append(int(args[1]))
    else:
        print("unknown action")

