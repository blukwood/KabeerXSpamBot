from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from kabeer import kabeercmd

MESSAGE = (
        'Hello there!\n'
        'I am a Spam Bot Build with Pyrogram and Python\n\n'
        'By [RhythmOfficial](https://t.me/RhythmOfficial)'
    )

KEYBOARD = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text='Support', callback_data='sele_pyrogram')],
    [InlineKeyboardButton(text='Updates', callback_data='sele_telethon')]]
)

@kabeercmd.on_message(filters.text & filters.private & ~filters.bot)
async def start(sessionCli, message):
    await message.reply(
        text=MESSAGE,
        reply_markup=KEYBOARD,
        disable_web_page_preview=False
    )
