
import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
import random


class TestBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + str(random.randint(1,10000)))

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        print(e)
        print('col')
        c.privmsg(e.target,text = "neat")
        return


def main():
    import sys

    bot = TestBot('#hello', 'thisbot', '10.13.13.2', 6667)
    bot.start()


if __name__ == "__main__":
    main()
