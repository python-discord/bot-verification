import logging

from discord.ext.commands import Bot, when_mentioned_or

from bot.constants import Bot as BotConfig


log = logging.getLogger(__name__)

bot = Bot(
    command_prefix=when_mentioned_or(
        "self.", "bot."
    ),
    case_insensitive=True
)

bot.load_extension("bot.cogs.security")
bot.load_extension("bot.cogs.verification")

bot.run(BotConfig.token)