#! ./.venv/bin/python3 
import os
from discord import Intents, Client, Message
from dotenv import load_dotenv
from loguru import logger
from utils.responses import generate_response
# load the token 
load_dotenv()
TOKEN: str = os.getenv('DISCORD_TOKEN')

# bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# message func
async def send_message(message:Message, user_message:str) -> None:
    if not user_message:
        logger.warning('empty message')
        return 
    if "/picoCTF" in user_message.split() : 
        try:
            response = generate_response(user_message)
            await message.channel.send(response)
        except Exception as e:
            logger.error(f'Error: {e}')

# bot startup 
@client.event
async def on_ready() -> None:
    logger.success(f'{client.user} has connected to Discord!')

# bot message handler
@client.event
async def on_message(message:Message) -> None:
    if message.author == client.user:
        return
    await send_message(message, message.content)

# run the bot
def main() -> None:
    client.run(TOKEN, log_handler=None)

if __name__ == "__main__":
    main()


