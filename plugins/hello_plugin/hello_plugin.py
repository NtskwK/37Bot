from ncatbot.plugin_system import NcatBotPlugin
from ncatbot.plugin_system import command_registry
from ncatbot.core.event import BaseMessageEvent


class HelloPlugin(NcatBotPlugin):
    name = "HelloPlugin"
    version = "1.0.0"

    async def on_load(self):
        pass

    @command_registry.command("hello")
    async def hello_cmd(self, event: BaseMessageEvent):
        await event.reply("Hello! I'm 37Bot.")

    @command_registry.command("help")
    async def help_cmd(self, event: BaseMessageEvent):
        help_text = "Available commands:\n/hello - Say hello\n/help - Show this help"
        await event.reply(help_text)
