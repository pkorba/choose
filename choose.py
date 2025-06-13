from maubot import Plugin, MessageEvent
from maubot.handlers import command
import random


class ChooseBot(Plugin):
    @command.new("choose", help="Have the bot choose for you")
    @command.argument("options", pass_raw=True, required=True)
    async def choose(self, evt: MessageEvent, options: str) -> None:
        await evt.mark_read()
        if not options:
            await evt.reply("> **Usage:** !choose <option1, option2, option3>")
            return
        options_array = options.split(",")
        choice = random.choice(options_array).strip()
        await evt.reply(f"> I choose **{choice}**.")
