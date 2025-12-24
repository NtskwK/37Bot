from ncatbot.core import BotClient
from ncatbot.core.event import GroupMessageEvent, PrivateMessageEvent

bot = BotClient()


@bot.on_group_message()
async def on_group_message(event: GroupMessageEvent):
    if event.raw_message == "ping":
        await event.reply("pong!")


@bot.on_private_message()
async def on_private_message(event: PrivateMessageEvent):
    if event.raw_message == "ping":
        await event.reply("pong!")


if __name__ == "__main__":
    bot.run_frontend()
