from pyrogram import filters, Client
import asyncio
from kabeer import kabeercmd
from pyrogram.types import Chat, User
from typing import ClassVar, Optional
from pyrogram.types import Message
import pyrogram
from kabeer.config import Config
from typing import Sequence

from typing import List, Union
import random
from kabeer import calls

from callsmusic import pytgcalls 


@kabeercmd.on_message(filters.command('vcraid'))
async def vcraid(_,message):
  try:
    await vcraidcmd.start()
  except:
    pass
  reply = message.reply_to_message
  if reply:
    msg = await message.reply('Processing...')
    path = await reply.download()
    await pytgcalls.join_group_call(message.chat.id)
    await pytgcalls.stream_audio(path , repeat=False)
    await msg.edit('AAJA VC BSDK, MAI BOLO GA AAB')
    
    
@kabeercmd.on_message(filters.command('stopvcraid'))    
async def stopvcraid(_,message):
  await calls.stop()
  await calls.leave_current_group_call()
