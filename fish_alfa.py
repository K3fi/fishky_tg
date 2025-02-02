import telebot
import random
from telebot import types

allfish = [0, 0, 0]
maney = 5000000000
user = [0, 0, 5, 1, 7, 2, 15, 0]
beer = 0




bot = telebot.TeleBot()

@bot.message_handler(commands= ["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Это бот-симулятор рыбалки \nВот команды: \n /fish - рыбачить \n/allfish - вся рыба \n/sale - продать рыбу")

if beer >= 1:
    @bot.message_handler(commands=["fish"])
    def alcofich(message):
        global allfish, user, beer, allfish
        if beer == 85:
            user[1] += 10
            user[2] += 10
            user[3] += 25
            user[4] += 25
            user[5] += 100
            user[6] += 100
            fish1 = random.randint(user[1], user[2])
            fish2 = random.randint(user[2], user[4])
            fish3 = random.randint(user[5], user[6])
            allfish[0] = allfish[0] + fish1
            allfish[1] = allfish[1] + fish2
            allfish[2] = allfish[2] + fish3
            user[7] += 1
            if user[7] >= 5:
                user -= 5
                user[0] -= 1
        
        elif beer >= 65:
            user[1] += 7
            user[2] += 7
            user[3] += 18
            user[4] += 18
            user[5] += 75
            user[6] += 75
            fish1 = random.randint(user[1], user[2])
            fish2 = random.randint(user[2], user[4])
            fish3 = random.randint(user[5], user[6])
            allfish[0] = allfish[0] + fish1
            allfish[1] = allfish[1] + fish2
            allfish[2] = allfish[2] + fish3
            user[7] += 1
            if user[7] >= 5:
                user[7] -= 5
                beer -= 1
        

        elif beer >= 45:
            user[1] += 5
            user[2] += 5
            user[3] += 14
            user[4] += 14
            user[5] += 50
            user[6] += 50
            fish1 = random.randint(user[1], user[2])
            fish2 = random.randint(user[2], user[4])
            fish3 = random.randint(user[5], user[6])
            allfish[0] = allfish[0] + fish1
            allfish[1] = allfish[1] + fish2
            allfish[2] = allfish[2] + fish3
            user[7] += 1
            if user[7] >= 5:
                user[7] -= 5
                beer -= 1
        

        elif beer >= 25:
            user[1] += 2
            user[2] += 2
            user[3] += 10
            user[4] += 10
            user[5] += 25
            user[6] += 25
            fish1 = random.randint(user[1], user[2])
            fish2 = random.randint(user[2], user[4])
            fish3 = random.randint(user[5], user[6])
            allfish[0] = allfish[0] + fish1
            allfish[1] = allfish[1] + fish2
            allfish[2] = allfish[2] + fish3
            user[7] += 1
            if user[7] >= 5:
                user[7] -= 5
                beer -= 1
        

        elif beer >= 1:
            user[1] += 1
            user[2] += 1
            user[3] += 5
            user[4] += 5
            user[5] += 12
            user[6] += 12
            fish1 = random.randint(user[1], user[2])
            fish2 = random.randint(user[2], user[4])
            fish3 = random.randint(user[5], user[6])
            allfish[0] = allfish[0] + fish1
            allfish[1] = allfish[1] + fish2
            allfish[2] = allfish[2] + fish3
            bot.send_message(message.chat.id, f"Вы выловили: \n{fish1} \n{fish2} \n{fish3} \n"
                                        f"Всего рыбы {allfish[0]}, {allfish[1]}, {allfish[2]}, алкаш на {beer} ")

        

    @bot.message_handler(commands=["sale"])
    def alcosalefish(message):
        global allfish, maney 
        money = 0

        for mon in range(allfish[0]):
            money = money + 2
            allfish[0] = allfish[0] - 1

        for mon in range(allfish[1]):
            money = money + 1.50
            allfish[1] = allfish[1] - 1
        
        for mon in range(allfish[2]):
            money = money + 1
            allfish[2] = allfish[2] - 1 
        maney += money

        bot.send_message(message.chat.id, f"Вы заработали {money}") 

elif beer <= 0:
    @bot.message_handler(commands=["fish"])
    def fish(message):
        global allfish, user
        fish1 = random.randint(user[1], user[2])
        fish2 = random.randint(user[2], user[4])
        fish3 = random.randint(user[5], user[6])
        allfish[0] = allfish[0] + fish1
        allfish[1] = allfish[1] + fish2
        allfish[2] = allfish[2] + fish3
        
        bot.send_message(message.chat.id, f"Вы выловили: \n{fish1} \n{fish2} \n{fish3} \n"
                                        f"Всего рыбы {allfish[0]}, {allfish[1]}, {allfish[2]} ")
 

    @bot.message_handler(commands=["sale"])
    def salefish(message):
        global maney
        money = 0

        for mon in range(allfish[0]):
            money = money + 1
            allfish[0] = allfish[0] - 1

        for mon in range(allfish[1]):
            money = money + 0.75
            allfish[1] = allfish[1] - 1
        
        for mon in range(allfish[2]):
            money = money + 0.50
            allfish[2] = allfish[2] - 1 
        maney += money

        bot.send_message(message.chat.id, f"Вы заработали {money}") 

@bot.message_handler(commands=["shop"])
def shoplist(message):
    bl = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("🎣", callback_data = "buyd")
    btn2 = types.InlineKeyboardButton("🐛", callback_data = "buyp")
    btn3 = types.InlineKeyboardButton("🏖️", callback_data = "buylo")
    btn4 = types.InlineKeyboardButton("🍺", callback_data = "beer")
    bl.add(types.InlineKeyboardButton("⚙️", callback_data = "settings"))
    bl.row(btn1, btn2)
    bl.row(btn3, btn4)

    bot.send_message(message.chat.id, f"Лавка у побережья \n \n"
                                        f"🎣 - удочки \n \n"
                                        f"🐛 - приманка \n \n"
                                        f"🏖️ - локации\n \n"
                                        f"🍺 - алкашка\n \n"
                                        f"⚙️ - настройки\n", reply_markup= bl)


@bot.message_handler(commands=["stats"])
def stats(message):
    bot.send_message(message.chat.id, f'{maney} ваши деньги ')

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "buyd":
        bl = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("🌳", callback_data = "wooby")
        btn2 = types.InlineKeyboardButton("🌵", callback_data = "kaktby")
        btn3 = types.InlineKeyboardButton("🔍", callback_data = "glasby")
        btn4 = types.InlineKeyboardButton("🛢️", callback_data = "plasby")
        bl.add(types.InlineKeyboardButton("➡", callback_data = "dalshe"))
        bl.row(btn1, btn2)
        bl.row(btn3, btn4)

        bot.send_message(callback.message.chat.id, f"Удочки: \n \n"
                                          f"🌳 - деревянная удочка: 5 000₽\n \n"
                                          f"🌵 - кактусовая удочка: 15 000₽\n \n"
                                          f"🔍 - стеклянная удочка: 75 000₽\n \n"
                                          f"🛢️ - пластиковая удочка: 145 000₽\n \n"
                                          f"➡ - металическая удочка \n", reply_markup=bl)
        
    elif callback.data == "wooby":
        global maney, user, beer
        if maney >= 5000:
            maney -= 5000
            user[1] = 2
            user[2] = 5
            user[3] = 3
            user[4] = 10
            user[5] = 5
            user[6] = 15
            bot.send_message(callback.message.chat.id, "Вы купили деревянную удочку")
        
        else:
            bot.send_message(callback.message.chat.id, "не хватает средств")

    elif callback.data == "kaktby":

        if maney >= 15000:
            maney -= 15000
            user[1] = 3
            user[2] = 7
            user[3] = 5
            user[4] = 12
            user[5] = 7
            user[6] = 15
            bot.send_message(callback.message.chat.id, "Вы купили кактусовую удочку")
        
        else:
            bot.send_message(callback.message.chat.id, "не хватает средств")
    
    elif callback.data == "glasby":
        
        if maney == 75000:
            maney -= 75000
            user[1] = 0
            user[1] = 8
            user[1] = 0
            user[1] = 12
            user[1] = 0
            user[1] = 16
            bot.send_message(callback.message.chat.id, "Вы купили стеклянную удочку")
        
        else:
            bot.send_message(callback.message.chat.id, "не хватает средств")

    if callback.data == "plasby":
        
        if maney >= 145000:
            maney -= 145000
            user[1] = 5
            user[1] = 10
            user[1] = 7
            user[1] = 15
            user[1] = 10
            user[1] = 20
            bot.send_message(callback.message.chat.id, "Вы купили пластиковую удочку")
        
        else:
            bot.send_message(callback.message.chat.id, "не хватает средств")

    if callback.data == "beer":
        bl = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("🍺", callback_data = "beerwhite")
        btn2 = types.InlineKeyboardButton("🥃", callback_data = "beernegr")
        btn3 = types.InlineKeyboardButton("🍶", callback_data = "vodka")
        btn4 = types.InlineKeyboardButton("💊", callback_data = "ass")

        bl.row(btn1, btn2)
        bl.row(btn3, btn4)
        bot.send_message(callback.message.chat.id, f"алкашка:\n \n"
                                                   f"🍺 - пиво светлое: 5000₽\n \n"
                                                   f"🥃 - пиво темное: 3500₽\n \n"
                                                   f"🍶 - водка: 7500₽\n \n"
                                                   f"💊 - эспирин: 5000₽\n \n", reply_markup=bl)

    if callback.data == "beerwhite":

        if maney >= 5000:
            maney -= 5000
            beer += 10
            bot.send_message(callback.message.chat.id, f'Вы пьяны на {beer}')
        else:
            bot.send_message(callback.message.chat.id, "Милорд, золото кончилось")

    if callback.data == "beernegr":

        if maney >= 3500:
            maney -= 3500
            beer += 15
            bot.send_message(callback.message.chat.id, f'Вы пьяны на {beer}')
        else:
            bot.send_message(callback.message.chat.id, "Милорд, золото кончилось")

    if callback.data == "vodka":
        if maney >= 7500:
            maney -= 7500
            beer += 50
            bot.send_message(callback.message.chat.id, f'Вы пьяны на {beer}')
        else:
            bot.send_message(callback.message.chat.id, "Милорд, золото кончилось")

    if callback.data == "ass":
        if maney >= 5000:
            maney -= 5000
            beer -= 20
            bot.send_message(callback.message.chat.id, f'Вы пьяны на {beer}')
        else:
            bot.send_message(callback.message.chat.id, "Милорд, золото кончилось")


bot.infinity_polling()
