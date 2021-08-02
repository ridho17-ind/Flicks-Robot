import random

from KanekiRobot import dispatcher
from KanekiRobot.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.ext import CallbackContext, run_async

reactions = [
        "🤤",
        "😂",
        "👌",
        "✌",
        "😎",
        "💞",
        "👍",
        "👌",
        "💯",
        "🎶",
        "👀",
        "😂",
        "👓",
        "👏",
        "👐",
        "🍕",
        "💥",
        "🍴",
        "💦",
        "💦",
        "🍑",
        "🍆",
        "😩",
        "😏",
        "😑",
        "👀",
        "👅",
        "😩",
        "🥵",
        "😈",
        "😣",
        "🥴",
        "👿",
        "🥰",
        "🥶",
        "🤡",
        "👻",
        "🔥",
        "😡",
        "😱",
        "🤭",
        "🗿",
        "🤬",
        "😜",
        "🤔",
        "😭",
        "❤️",
        "🎯",
        "🥺",
        "🧼",
]


@run_async
def react(update: Update, context: CallbackContext):
    message = update.effective_message
    react = random.choice(reactions)
    if message.reply_to_message:
        message.reply_to_message.reply_text(react)
    else:
        message.reply_text(react)


REACT_HANDLER = DisableAbleCommandHandler("react", react)

dispatcher.add_handler(REACT_HANDLER)

__command_list__ = ["react"]
__handlers__ = [REACT_HANDLER]
