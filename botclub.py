# -*- coding: utf-8 -*-
#################################
#
# Bot per Telegram del Club de Programació de Casp
#
# Programat per Sergi Gilabert Sempere
#
# ©2016 Club de Programació de Casp. Versió 0.2
#
# http://sites.google.com/a/fje.edu/clubdeprogramaciocasp
#
#####################################

import telebot
from telebot import types
import time

TOKEN = "" #Insert here the Token given by @BotFather

f = open("usuaris.txt", "r+") #You have to change usuaris.txt with the file you'll use to save the user's chat ID
admin = "XXXXXXX" #Here you have to change it with the bot admin's ID
usuaris = [line.rstrip('\n') for line in f]

bot = telebot.TeleBot(TOKEN)

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            cid = m.chat.id
            print("[" + str(cid) + "]: " + m.text)

bot.set_update_listener(listener)

@bot.message_handler(commands=['start'])
def command_benvinguda(m):
    cid = m.chat.id
    IDlist = f.read()
    if not str(cid) in usuaris:
        usuaris.append(str(cid))
        f.write(str(cid)+"\n") #Here the user's ID will be registered to the file with all the user's ID
        bot.send_message(cid, "Gràcies per utilitzar el servei. Mitjançant aquest bot pots justificar absències i confirmar assistència a l'Aula Oberta.")
    else:
        bot.send_message(cid, "Ja estàs registrat, no fa falta que tornis a executar aquest comandament.")
    f.close()
#this command is the first command executed. It's used to save the user's ID to the user's file.

@bot.message_handler(commands=['assistir'])
def command_assistir(m):
    cid = m.chat.id
    name = m.chat.first_name
    lastName = m.chat.last_name
    dia = m.text[9:]
    user = m.chat.username
    bot.send_message(cid, "Gràcies " + name + "! La teva assistència està confirmada. En cas de no poder assistir et preguem que ens ho comuniquis mitjançant el comandament /absencia acompanyat de la data (en format DD/MM) i aula oberta. (ex: /absencia 19/09 aula oberta)")
    bot.send_message(admin, name+" "+lastName+" vindrà a l'Aula Oberta el dia "+dia+". En cas de cancel·lar-se contacta amb l'alumne mitjançant @" + user)
#this command is used by a student to communicate to the admin (someone of the club) that he'll come to class

@bot.message_handler(commands=['absencia'])
def command_absencia(m):
    cid = m.chat.id
    name = m.chat.first_name
    lastName = m.chat.last_name
    message = name + " " + lastName + " no podrà assistir a la classe de " + m.text[16:] + " el dia " + m.text[9:15]
    bot.send_message(admin, message)
    bot.send_message(cid, "La teva absència ja s'ha comunicat a un responsable. Gràcies per comunicar-ho!")
#this command is used by a student to communicate to the admin (someone of the club) that he won't come to class

@bot.message_handler(commands=['contacta'])
def command_contacta(m):
    cid = m.chat.id
    user = m.chat.username
    if str(cid) != str(admin):
        try:
            bot.send_message(admin, m.text[9:]) #the admin will receive the message
            bot.send_message(admin, "  / sent by @" + user + " / ") #it tells the admin who sent the message
            bot.send_message(cid, "El missatge s'ha enviat correctament, et respondrem en breus.")
        except:
            bot.send_message(cid, "El missatge no s'ha enviat correctament. Prova-ho més tard.")
    elif str(cid) == str(admin): #if the user is admin, it will send a message to every user of the user's file
        for ID in usuaris:
            try:
                bot.send_message(int(ID), m.text[9:]) #the message is what comes after the command
            except:
                bot.send_message(cid, "El missatge no s'ha enviat correctament. Comprova la consola del servidor.")
        bot.send_message(cid, "El missatge s'ha enviat correctament")

#this command is used by a student to communicate something to the club and by an admin (someone of the club) to send a message to everybody of the user's file

bot.polling(none_stop=True) #it's used so the bot will never stop working
