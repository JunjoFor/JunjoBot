import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from telegram import *  # Aquí lo estoy importando todo, pero podrías importar solo lo que necesites
from telegram.ext import *

import main

mapaUsuarios = {}

def baseInit():
    global mapaUsuarios
    cred = credentials.Certificate('junjobot-firebase-adminsdk-gu0ld-9937249398.json')
    firebase_admin.initialize_app(cred)
    #data = {
    #'id' : '2345',
    #'count' : 0
    #}
    db = firestore.client()
    users_ref = db.collection('Users')
    docs = users_ref.stream()

    for doc in docs:
            mapaUsuarios[doc.to_dict().get('name')] = (doc.to_dict())

    return mapaUsuarios
def registerUser(update: Update, context: CallbackContext):
    db = firestore.client()
    user = update.effective_message.from_user
    data = {
    'id' : user.id,
    'count' : 0,
    'name' : user.username
    }
    try:
        db.collection('Users').document(user.username).set(data)
        update.message.reply_text('Se ha registrado con éxito')
        mapaUsuarios[user.username] = data
    except Exception as e:
        print(e)
        update.message.reply_text('Error')


def contador(update: Update, context: CallbackContext):
    user = update.effective_message.from_user
    db = firestore.client()
    counter = mapaUsuarios[user.username].get('count') + 1
    mapaUsuarios[user.username]['count'] = counter
    try:
        db.collection('Users').document(user.username).update({'count' : counter})
        mapaUsuarios[user.username]['count'] = counter
        update.message.reply_text(f'ahora su contador es de {counter}')
    except Exception as e:
        print(e)
        update.message.reply_text('ha ocurrido un error')

def contadorInfo(update: Update, context: CallbackContext):
    user = update.effective_message.from_user
    counter = mapaUsuarios[user.username].get('count')
    update.message.reply_text(f'llevas {counter} pajas')
