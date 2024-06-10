#! ./.venv/bin/python3 
import os
from discord import Intents, Client, Message
from dotenv import load_dotenv
from typing import Final
from loguru import logger

# load the token 
load_dotenv()
TOKEN: Final["str"] = os.getenv('DISCORD_TOKEN')

# bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# message func
async def send_message(message:Message, user_message:str) -> None:
    if not user_message:
        print('empty message')
        return 
    if "/rank" in user_message : 
        try:
            await message.channel.send("here's your rank")
        except Exception as e:
            print(e)

# bot startup 
@client.event
async def on_ready() -> None:
    logger.success(f'{client.user} has connected to Discord!')

# bot message handler
@client.event
async def on_message(message:Message) -> None:
    if message.author == client.user:
        return
    author: str = str(message.author)
    channel:str = str(message.channel)

    logger.info(f'Received message from {author} in {channel}')
    await send_message(message, message.content)

# run the bot
def main() -> None: 
    client.run(TOKEN, log_handler=None)

if __name__ == "__main__":
    main()


