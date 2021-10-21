from pyrogram import Client
from pyromod import listen
from kabeer.config import Config
import logging
from pytgcalls import PyTgCalls


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

LOGGER = logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Init session
API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN
LOG_CHANNEL = Config.LOG_CHANNEL
SESSION = Config.SESSION

kabeercmd = Client(
    'botSession',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(
        root='kabeer.pl'
    )
)


vcraidcmd = Client(SESSION, api_id=API_ID, api_hash=API_HASH)


calls = PyTgCalls(vcraidcmd)
