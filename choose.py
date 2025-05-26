from maubot import Plugin, MessageEvent
from maubot.handlers import command
import random


class ChooseBot(Plugin):
    @command.new("choose", help="Have the bot choose for you")
    @command.argument("choose_text", pass_raw=True)
    async def echo_handler(self, evt: MessageEvent, choose_text: str) -> None:
        await evt.mark_read()
        choose_array = choose_text.split(",")
        choose_reply = random.choice(choose_array).strip()
        await evt.reply(f"I choose **{choose_reply}**.")
