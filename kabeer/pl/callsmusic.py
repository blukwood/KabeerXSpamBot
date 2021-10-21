from config import Config
import pytgcalls
from pyrogram import Client 

vcraid = Client(SESSION_NAME, API_ID, API_HASH)
pytgcalls = PyTgCalls(vcraid)

run = pytgcalls.run
