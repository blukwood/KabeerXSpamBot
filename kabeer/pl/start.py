from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from kabeer import exploiter

MESSAGE = (
        'Hello there!\n'
        'I am a Spam Bot Build with Pyrogram and Python\n\n'
        'By [RhythmOfficial](https://t.me/RhythmOfficial)'
    )

KEYBOARD = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text='Support', url='https://t.me/RhythmOff')],
    [InlineKeyboardButton(text='Updates', url='https://t.me/RhythmOfficial')]]
)

@exploiter.on_message(filters.text & filters.private & ~filters.bot)
async def start(sessionCli, message):
    await message.reply(
        text=MESSAGE,
        reply_markup=KEYBOARD,
        disable_web_page_preview=True
    )
