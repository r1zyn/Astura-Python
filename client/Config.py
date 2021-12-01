import os
import discord
from dotenv import load_dotenv
load_dotenv()

configOptions = {
    "clientID": os.environ["CLIENT_ID"],
    "clientOptions": {
        "intents": discord.Intents.all()
    },
    "clientSecret": os.environ["CLIENT_SECRET"],
    "owners": ["760995822120468511", "752114457202917436"], # Ascendus, lucaslah
    "token": os.environ["TOKEN"]
}