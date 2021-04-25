from telegram import *  # Aquí lo estoy importando todo, pero podrías importar solo lo que necesites
from telegram.ext import *
from dataBase import mapaUsuarios
import requests
import json


def prueba():
    while True:
        nickname = 'TheJuanjo234'
        headers = {'Authorization': 'Token 638cd808e13d325a090038dc38104a17122d3093'}
        r = requests.get(f'https://hanzoweb.herokuapp.com/fiumcraft/api/userdata?nickname={nickname}', headers=headers)
        dictionary = json.loads(r.content)
        if(dictionary.get('nickname') != 'TheJuanjo234'):
            print(dictionary)
            break

# hacer muteo cuando insulten al bot


def getFiumcraft(nickname):
    headers = {'Authorization': 'Token 638cd808e13d325a090038dc38104a17122d3093'}
    r = requests.get(f'https://hanzoweb.herokuapp.com/fiumcraft/api/userdata?nickname={nickname}', headers=headers)
    dictionary = json.loads(r.content)
    return dictionary
    # {'error': 'texto'}
    # {'warning': 'warningstr'}


def getDinero(nickname):
    dictionary = getFiumcraft(nickname)
    return dictionary.get('money')


def getOnline(nickname):
    dictionary = getFiumcraft(nickname)
    return dictionary.get('lastSeen')


def getOnlineTownList(nickname):
    dictionary = getFiumcraft(nickname)
    residentList = dictionary.get('residents')

    list = []
    for r in residentList:
        online = getOnline(r)
        if('online' in online):
            list.append(r)
    print(list)
    return list


def onlineTown(update: Update, context: CallbackContext):
    args = context.args
    user = update.effective_message.from_user
    if not args:
        respuesta = 'tienes que escribir /onlineTown (username)'
        lista = getOnlineTownList(mapaUsuarios[user.username].get('minecraftName'))
    else:
        respuesta = 'Estan online los siguientes jugadores:\n'
        lista = getOnlineTownList(args[0])
    try:

        if len(lista) > 0:
            for o in lista:
                respuesta += str(o) + '\n'
        else:
            respuesta = 'no hay nadie conectado ahora mismo'
    except Exception as e:
        respuesta = 'ERROR 🐡'
        print(f'ERROR EN onlineTown: {e}')
    update.message.reply_text(respuesta)


def moneyRankDic(nickname):
    dictionary = getFiumcraft(nickname)
    residentList = dictionary.get('residents')

    map = {}
    for r in residentList:
        map[r] = getDinero(r).replace(',', '')

    mapSorted = {k: v for k, v in sorted(map.items(), key=lambda item: float(item[1][:-1]), reverse=True)}
    print(mapSorted)
    return mapSorted


def moneyCity(update: Update, context: CallbackContext):
    args = context.args

    if not args:
        respuesta = 'tienes que escribir /moneyTown (username)'
    else:
        try:
            dictionary = getFiumcraft(args[0])
            respuesta = str(dictionary.get('moneyInBank'))
        except:
            respuesta = 'error 🐡'
    update.message.reply_text(respuesta)


# respuesta = getFiumcraft('TheJuanjo234')
# print(respuesta)
# print(str(respuesta.get('money')) + '€')
