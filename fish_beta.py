import telebot
import sqlite3
import random
from telebot import types

bot = telebot.TeleBot("7124793024:AAG3cmFwLmd2QBGayCKugouH1-03epP8NEI")

USERS = [0, "" ]
maney = 0
ex = 0
frod = "wood_rod"
bait = 0



@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.username
    database = sqlite3.connect("database.sql")
    cur = database.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, maney int, frod varchar(50), ex int, bait int, name varchar(50))")
    database.execute(f"INSERT INTO users (maney, frod, ex, bait, name) VALUES ('%s', '%s', '%s', '%s', '%s')" % (maney, frod, ex, bait, name))
    USERS[0] = cur.execute("SELECT id FROM users")
    database.commit()
    cur.close()
    database.close()

    bot.send_message(message.chat.id, f"Рыбалка версии 2 ")

@bot.message_handler(commands=["userss"])
def topuser(message):
    database = sqlite3.connect("database.sql")
    cur = database.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    info = ""
    for el in users:
            info += f"Имя: {el[5]}\n"

    cur.close()
    database.close()
    bot.send_message(message.chat.id, info)

bot.infinity_polling()