from config import Config
import pytgcalls
from pyrogram import Client 

SESSION = Config.SESSION 
API_ID = Config.API_ID 
API_HASH = Config.API_HASH

vcraid = Client(SESSION, API_ID, API_HASH)
pytgcalls = PyTgCalls(vcraid)

run = pytgcalls.run
