from discord.ext import commands
from Config import configOptions
from Configuration import Configuration
from Utilities import Utilities

class AsturaClient(commands.Bot):
    def __init__(self, command_prefix: str = "!="):
        super(command_prefix)
        self.config: Configuration = Configuration(configOptions)
        self.util: Utilities = Utilities(self)


    def start(self):
        self.login(self.config.token)