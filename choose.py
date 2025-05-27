from maubot import Plugin, MessageEvent
from maubot.handlers import command
import random


class ChooseBot(Plugin):
    @command.new("choose", help="Have the bot choose for you")
    @command.argument("choices", pass_raw=True, required=True)
    async def choose(self, evt: MessageEvent, choices: str) -> None:
        await evt.mark_read()
        if not choices:
            await evt.respond("Usage: !choose <choice1, choice2, choice3>")
            return
        choices_array = choices.split(",")
        choice = random.choice(choices_array).strip()
        await evt.reply(f"I choose **{choice}**.")
