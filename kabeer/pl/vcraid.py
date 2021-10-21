from pyrogram import filters, Client
import asyncio
from kabeer import kabeercmd, vcraidcmd
from pyrogram.types import Chat, User
from typing import ClassVar, Optional
from pyrogram.types import Message
import pyrogram
from kabeer.config import Config
from typing import Sequence

from typing import List, Union
import random

@kabeercmd.on_message(filters.command('vcraid'))
@vcraidcmd.on_message(filters.command('raid'))
async def vcraid(client: Client, message: Message):
    message.reply("Hey", parse_mode=None)
