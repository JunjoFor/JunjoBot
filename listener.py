from telegram import *
from telegram.ext import *
from telegram.ext.dispatcher import run_async
from spellingChecker import *
import re
from dataBase import *
contador = 0

# Podría venirme bien utilizar Pycairo


def listener(update: Update, context: CallbackContext):

    global contador
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
    message = eliminarTildes(message)
    message = spellingChecker(message)
    words = message.replace('?', '').replace(',', '').replace('!', '').split()
    lenWords = len(words)
    chatTitle = update.effective_message.chat.title
    replyToMessage = update.message.reply_to_message  # Si el mensaje está respondiendo a otro, podrás acceder a él con replyToMessage.text

    # if ('furro' in message):
    # permisos = ChatPermissions(can_send_messages=False, can_send_media_messages=False, can_send_polls=False, can_send_other_messages=False, can_add_web_page_previews=False, can_change_info=False, can_invite_users=False, can_pin_messages=False)
    # update.effective_message.reply_text('ban por furrx')
    # bot.promoteChatMember(chatID, user.id, can_change_info=False, can_post_messages=False, can_edit_messages=False, can_delete_messages=False, can_invite_users=False, can_restrict_members=False, can_pin_messages=False, can_promote_members=False, is_anonymous=False, can_manage_chat=False, can_manage_voice_chats=False)
    # bot.kickChatMember(chatID, user.id)
    # print(user.username + 'ha sido echado por ser furro')
    if('hola' in message and priv):
        update.effective_message.reply_text('hola ' + user.username)
    if('pecaminosa' in message or 'pecaminoso' in message):
        update.effective_message.reply_text('echado porque si')
        print(user.username + 'ha sido echado porque si')
        bot.kickChatMember(chatID, user.id)
    if('todo mal' in message):
        bot.send_voice(chatID, open('./todoMal.ogg', 'rb'))
    if ('sexo' in message):
        bot.send_video(chatID, open('./sexo.mp4', 'rb'))
    if('nomura' in message):
        update.effective_message.reply_text('Nomura cabrón')
    if 'eduardo' in message:
        bot.send_photo(chatID, open('./eduardo.png', 'rb'))
    if('urraca' in message):
        bot.send_voice(chatID, open('./urraca.ogg'))
    elif 'depression' in message:
        bot.send_photo(chatID, open('./depression.jpg', 'rb'))
    if ('hola junjobot' in message):
        update.effective_message.reply_text('hola ' + user.username)
    if user.username == "junjou" or user.username in mapaUsuarios.name:
        pass
    elif ('junjobot gilipollas' in message or 'gilipollas junjobot' in message):
        update.effective_message.reply_text('a insultar a tu madre, ' + user.username)
    elif lenWords <= 3 and re.search(r'hol[ia]', message):
        update.effective_message.reply_text('Hola!')
    elif('adios' in message):
        update.effective_message.reply_text('bueno adios master')

    elif ('puta' in words):
        update.effective_message.reply_text('Puta tu madre')
    elif ('zorra' in message):
        update.effective_message.reply_text('Zorra tu madre')

    elif ('me cago en' in message):
        update.effective_message.reply_text('yo me cago en tus muertos pisados a caballo')
    elif (('warrah' or 'warra') in message and lenWords == 1):
        update.effective_message.reply_text('warrah')
    elif ('ano' in words[lenWords - 1][-3:]):
        update.effective_message.reply_text('Me la agarras con la mano')
    elif ('cinco' in words[lenWords - 1][-5:]):
        update.effective_message.reply_text('Por el culo te la hinco')
    elif ('rita' in words[lenWords - 1][-4:]):
        update.effective_message.reply_text('La zorrita')
    elif 'ino' in words[lenWords - 1][-3:]:
        update.effective_message.reply_text('En tu culo mi pepino')
    elif 'trece' in words[lenWords - 1][-5:]:
        update.effective_message.reply_text('Agarramela que me crece')
