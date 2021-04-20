from telegram import *
from telegram.ext import *
from telegram.ext.dispatcher import run_async
import re


def listener(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    user = update.effective_message.from_user
    chatID = update.effective_message.chat_id
    if update.edited_message:
        edited = True
        message = update.edited_message
    else:
        edited = False
        message = update.message.text

    user = update.message.from_user
    chatID = update.message.chat_id
    priv = chatID > 0

    message = message.lower()
    # message = eliminarTildes(message)
    # message = spellingChecker(message)
    words = message.replace('?', '').replace(',', '').replace('!', '').split()
    lenWords = len(words)
    chatTitle = update.effective_message.chat.title

    replyToMessage = update.message.reply_to_message  # Si el mensaje está respondiendo a otro, podrás acceder a él con replyToMessage.text

    if ('hola junjobot' in message):
        update.effective_message.reply_text('hola ' + user)
    elif lenWords <= 3 and re.search(r'hol[ia]', message):
        update.effective_message.reply_text('Hola!')

    elif ('puta'in message):
        update.effective_message.reply_text('Puta tu madre')

    elif ('zorra'in message):
        update.effective_message.reply_text('Zorra tu madre')
    elif ('me cago en' in message):
        update.effective_message.reply_text('yo me cago en tus muertos pisados a caballo')
    if ('ano'in words[lenWords-1][-3:]):
        update.effective_message.reply_text('Me la agarras con la mano')
    elif ('inco'in message):
        update.effective_message.reply_text('Por el culo te la hinco')
