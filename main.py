#!/usr/bin/env python3
from telegram import *  # Aquí lo estoy importando todo, pero podrías importar solo lo que necesites
from telegram.ext import *
from pueblo import *
from dataBase import *

import os
import sys
from threading import Thread
from time import sleep
from random import randint
import logging

import listener

# Enable logging
logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Variables del programa



def start(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    user = update.effective_message.from_user
    chatID = update.effective_message.chat_id
    if not args:
        # https://t.me/HanzoBot?start=TOKEN
        # Si alguien hace click en un enlace como ese y le da a "Start", tu bot recibirá el TOKEN en args
        pass

    bot.send_chat_action(chatID, action=ChatAction.TYPING)  # Para que salga que el bot está "escribiendo"
    sleep(1)
    bot.sendMessage(chatID, 'Hola!')  # Puedes meterle botones, markdown, html... Si quieres saber cómo, avísame
    update.message.reply_text('Hola pero respondiendo al mensaje')  # Aquí igual ^
    logger.info("%s (%s ~ %s) -> /start", user.name, user.id, chatID)


def d(update: Update, context: CallbackContext):
    'Función para tirar dados con /d\n'
    '- /d           Tira un dado de 20'
    '- /d X         Tira un dado de X'
    bot = context.bot
    args = context.args
    user = update.effective_message.from_user
    chatID = update.effective_message.chat_id
    if not args:
        result = str(randint(1, 20))
    else:
        try:
            result = str(randint(1, int(args[0])))
        except:
            result = 'ERROR 🐡'
    update.message.reply_text(result)

def moneyRank(update: Update, context: CallbackContext):
    args = context.args
    if not args:
        result = 'el comando /moneyRank necesita el campo (nickname)'
    else:
        try:
            dictionaty = moneyRankDic(args[0])

            result = ''

            for key in dictionaty:
                result += key + ' ' + str(dictionaty.get(key)) + "\n"
        except:
            result = 'ERROR 🐡'

    update.message.reply_text(result)

def money(update: Update, context: CallbackContext):
    'Función que devuelve tu dinero'

    bot = context.bot
    args = context.args
    user = update.effective_message.from_user
    chatID = update.effective_message.chat_id
    if not args:
        update.message.reply_text('El comando /money necesita el campo (nickname)')
    else:
        try:
            print(args[0])
            result = getDinero(args[0])
        except Exception as e:
            result = 'ERROR 🐡'
            print(f'ERROR EN MONEY: {e}')
        update.message.reply_text(result)

def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, error)


def otherUpdates(update: Update, context: CallbackContext):
    m = update.message
    '''
    A esta función llegan todos los updates de cosas como:
    Nosequien ha salido del grupo
    Nosequien ha entrado al grupo
    El grupo X se ha convertido en supergrupo (Hasta hace 2 actualizaciones,
    cuando ocurría esto cambiaba la ID del grupo, pero ahora (de cara al usuario)
            los superrupos no existen y, no estoy seguro de si se cambia la ID)
    '''


def help(update: Update, context: CallbackContext):
    result = 'Los comandos de este bot son: \n /money (nickname) te muestra tu dinero \n /moneyTown (nickname) te muestra el dinero de tu ciudad \n /moneyRank (nickname) te muestra un ranking de mayor a menor del dinero de cada integrante de la ciudad'
    update.message.reply_text(result)

def main(version=0):

    #prueba()
    if version == 0:
        updater = Updater('1738988045:AAEZwuOoUGS4GgzCqaK6POto0W9bSA5-74Y', use_context=True)  # El TOKEN de BotFather
    else:
        updater = Updater('1773961023:AAFlIJkxglNipQ0HwOsPM-d2l9wwBFsxav0', use_context=True)

    j = updater.job_queue  # Si necesitas pasarle el job_queue a alguna función, aquí lo tienes
    dp = updater.dispatcher  # No tienes que tocar esto

    baseInit()
    print(mapaUsuarios)
    def addC(filter, handler, **args):  # Esto lo he creado por comodidad
        dp.add_handler(CommandHandler(filter, handler, **args))

    def addM(filter, handler, **args):  # Esto lo he creado por comodidad
        dp.add_handler(MessageHandler(filter, handler, **args))

    # dp.add_handler(CallbackQueryHandler(button.button, pass_job_queue=True)) - Otros ejemplos
    # dp.add_handler(InlineQueryHandler(inline.inlinequery)) - Otros ejemplos
    addC('start', start, run_async=True)  # Con addC añades un handler para comandos ("/") y con addM para recibir todos los mensajes
    # Con pass_args le indicas que quieres los parámetros que se le pasen a /start

    # Con edited_updates recibirás también los updates de los mensajes editados
    #addC('d', d, run_async=True)
    addC('money', money, run_async=True)
    addC('moneyRank',moneyRank,run_async=True)
    addC('moneyTown',moneyCity,run_async=True)
    addC('onlineTown',onlineTown,run_async=True)
    addC('help',help,run_async=True)
    addC('register',registerUser,run_async=True)
    addC('paja',contador,run_async=True)
    addC('pinfo',contadorInfo,run_async=True)
    addM(Filters.text, listener.listener, run_async=True)  # En este caso le llegan los mensajes de texto a la función listener del módulo listener



    def stop_and_restart():
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(update: Update, context: CallbackContext):
        update.message.reply_text('Restarting')
        Thread(target=stop_and_restart).start()

    addC('restart', restart, filters=Filters.user(username='@juanyisus'))
    '''
    Con este filtro limitas que esa función solo pueda ser usada por tu username
    (aunque yo siempre hago una comprobación manual del ID dentro de la función)
    '''

    # log all errors
    #dp.add_error_handler(error)

    addM(Filters.all, otherUpdates)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
