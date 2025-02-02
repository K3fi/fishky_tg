import telebot
import sqlite3
import random
from telebot import types

bot = telebot.TeleBot()
fish = [0, 0, 0, 0, 0, 0]
locals = ["лужа", "Карп", "Серебряный карась", "Линь", 4, 3, 2]
name = ""
fishing = [0, 5, 2, 7, 5, 10]
maney = 0
ex = [0, 0, 0, 1500]
frod = "деревяннаяУдочка"
bait = [0, 0, 0, 0, 0, 0, 0, 0, 0]
alco = [1, 0]

class list():
    tov = ["", "", "", "", "", "", "", "", ""]
    text = ""
    rodb = ["", ""]
    fishin = [0, 0,0 , 0, 0,0, 0 ]
    def a(self, message):
        bl = types.InlineKeyboardMarkup()
        tov_len = len(self.tov)

        for i in range(min(4, tov_len // 2)):
            if 2*i < tov_len and 2*i + 1 < tov_len and 2*i + 4 < tov_len and 2*i + 5 < tov_len:
                btn1 = types.InlineKeyboardButton(self.tov[2*i], callback_data = self.tov[2*i + 4])
                btn2 = types.InlineKeyboardButton(self.tov[2*i + 1], callback_data = self.tov[2*i + 5])
                bl.row(btn1, btn2)
            else:
                break
        bl.add(types.InlineKeyboardButton("➡", callback_data=self.tov[8]))

        bot.send_message(message.chat.id, self.text, reply_markup=bl)

    def byrod(self, call):
        global maney, frod, fishing
        if maney >= self.fishin[6]:
            maney -= self.fishin[6]
            frod = self.rodb[0]
            fishing[0] = self.fishin[0]
            fishing[1] = self.fishin[1]
            fishing[2] = self.fishin[2]
            fishing[3] = self.fishin[3]
            fishing[4] = self.fishin[4]
            fishing[5] = self.fishin[5]
            bot.send_message(call.message.chat.id, self.rodb[1])
        else:
            bot.send_message(call.message.chat.id, "не хватает средств")

listbt = list()

#просто команды
@bot.message_handler(commands="fish")
def fishi(message):
    marcup = types.ReplyKeyboardMarkup(row_width=5)
    marcup.add(types.KeyboardButton("/fish"))
    marcup.add(types.KeyboardButton("/sale"))

    global fish,maney, alco, locals, bait
    fish[0] = random.randint(fishing[0], fishing[1]) + (bait[6] + bait[7] + bait[8]) + bait[5]
    fish[1] = random.randint(fishing[2], fishing[3]) + (bait[6] + bait[7] + bait[8]) + bait[5]
    fish[2] = random.randint(fishing[4], fishing[5]) + (bait[6] + bait[7] + bait[8]) + bait[5]
    fish[3] += fish[0]
    fish[4] += fish[1]
    fish[5] += fish[2]
    ex[0] = random.randint(15, 30)
    ex[1] += ex[0] * alco[0]

    if bait[0] >= 1:
        bait[0] -= 1
        if bait[0] == 0:
            bait[6] = 0
        else:
            pass

    elif bait[1] >= 1:
        bait[1] -= 1
        if bait[1] == 0:
            bait[7]= 0
        else:
            pass

    elif bait[2] >= 1:
        bait[2] -= 1
        if bait[2] == 0:
            bait[8] = 0
        else:
            pass



    if alco[1] >= 0.5:
        alco[1] -= 0.5

    elif ex[1] >= ex[3]:
        ex[3] *= 1.5
        ex[2] += 1
        ex[1] -= ex[3]
        maney += 5000
        
        if alco[1] >= 100:
            bot.send_message(message.chat.id, f"Вы набухались и умерли. С вас снято 50.000")
            maney -= 50000
        else:
            bot.send_message(message.chat.id, f"Вы выловили \n🐡{locals[1]} - {fish[0]}\n🐠{locals[2]} - {fish[1]}\n🐟{locals[3]} - {fish[2]}\nВcего рыбы {fish[3], fish[4], fish[5]} \n\nВы заработали {ex[0]} опыта", reply_markup= marcup)
    else:
        if alco[1] >= 100:
            bot.send_message(message.chat.id, f"Вы набухались и умерли. С вас снято 50.000")
            alco[1] = 0
            maney -= 50000
        else:
            bot.send_message(message.chat.id, f"Вы выловили \n🐡{locals[1]} - {fish[0]}\n🐠{locals[2]} - {fish[1]}\n🐟{locals[3]} - {fish[2]}\nВcего рыбы {fish[3], fish[4], fish[5]} \n\nВы заработали {ex[0]} опыта", reply_markup= marcup)

@bot.message_handler(commands=["stats"])
def stats(message):
    global ex, name, maney, frod, bait
    bot.send_message(message.chat.id, f"Статистика {name} \nУровень: {ex[2]} \nOпыта: {ex[1]} \nДенег: {maney} \nУдочка: {frod}\nПьяны на {alco[1]}\nУровень красноречия {alco[0]}\nМесто: {locals[0]}\nХлеба: {bait[0]}\nЧервяков: {bait[1]}\nМагнитов: {bait[2]}")


@bot.message_handler(commands=["sale"])
def salefish(message):
    global maney, locals
    money = 0

    for mon in range(fish[3]):
        money += locals[4] * alco[0]
        fish[3] -= 1

    for mon in range(fish[4]):
        money += locals[5] * alco[0]
        fish[4] -= 1
    
    for mon in range(fish[5]):
        money += locals[6] * alco[0]
        fish[5] -= 1
    maney += money

    bot.send_message(message.chat.id, f"Вы заработали {money} и всего {maney}") 

@bot.message_handler(commands=['shop'])
def shop(message):
    listbt.tov = ["🏖", "🍺", "🎣", "🐛", "homebt", "drinkbt", "rodbt", "baitbt", "dalshop"]
    listbt.text = "🏖 локации \n🍺 алко \n🎣 удочки \n🐛 наживки "
    listbt.a(message)

#события кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global maney, frod, fishing
    if call.data == "rodbt": # переход в меню удочек
        listbt.tov = ["🌲", "🎋", "🌵", "🌽", "woodrodby", "bamborodby", "cactooby", "cornrodby", "dalshoprod"]
        listbt.text = "🌲 сосновая удочка 20.000 \n🎋 бамбуковая удочка 40.000 \n🌵 кактусовая удочка 80.000\n🌽 кукурузная удочка 160.000"
        listbt.a(call.message)

    elif call.data == "baitbt":
        listbt.tov = ["🍞", "🐛", "🧲", "🦈", "breadby", "wormsby", "magnetby","sharkby", "dalshebtworms"]
        listbt.text = "🍞 хлеб 10x50\n🐛 червяк(да это гусеница) 25x50\n🧲 магнит 50x50\n🦈 акула(питомец) 999.999.999.999.999x1"
        listbt.a(call.message)
    
    elif call.data == "breadby":
        global maney, alco, locals
        bait[0] += 50
        maney -= 500
        bait[6] = 1
        bot.send_message(call.message.chat.id ,"Вы купили хлеб для наживки")
        
    elif call.data == "wormsby":
        bait[1] += 50
        maney -= 1250
        bait[7] = 1
        bot.send_message(call.message.chat.id ,"Вы купили червяка для наживки")

    elif call.data == "magnetby":
        bait[2] += 50
        maney -= 2500
        bait[8] = 1
        bot.send_message(call.message.chat.id ,"Вы купили фолшебный магнит для наживки")
        
    elif call.data == "sharkby":
        if maney >= 99999999999999999:
            bait[3] += 50
            maney -= 99999999999999999
            bait[5] == 99999999999999999
            bot.send_message(call.message.chat.id ,"Вы прошли игру! Поздравляю! Теперь акула ловит рыбу вместо вас")
        else:
            bot.send_message(call.message.chat.id ,"Вы бомж")


    elif call.data == "woodrodby":
        listbt.rodb = ["сосноваяУдочка", "Вы купили сосновую удочку!"]
        listbt.fishin = [1, 5, 3, 7, 7, 10, 7500]
        listbt.byrod(call)

    elif call.data == "bamborodby":
        listbt.rodb = ["бамбуковаяУдочка", "Вы купили бамбуковую удочку!"]
        listbt.fishin = [3, 5, 5, 7, 9, 10, 17000]
        listbt.byrod(call)


    elif call.data == "cactooby":
        listbt.rodb = ["кактусоваяУдочка", "Вы купили кактусовую удочку"]
        listbt.fishin = [4, 7, 7, 10, 9, 11, 25000]
        listbt.byrod(call)

    elif call.data == "cornrodby":
        listbt.rodb = ["кукурузнаяУдочка", "Вы купили кукурузную удочку!"]
        listbt.fishin = [6, 8, 8, 11, 11, 15, 50000]
        listbt.byrod(call)

    elif call.data == "drinkbt":
        listbt.tov = ["🍺", "🍸", "🥃", "🍷", "beerby", "mahitoby", "elby", "wineby", "alcodalshoprod"]
        listbt.text = "🍺 пиво 550 \n🍸 махито 1000\n🥃 эль 800 \n🍷 вино 400"
        listbt.a(call.message)

    elif call.data == "beerby":
        alco[1] += 4
        maney -= 550
        if 1 <= alco[1] <= 10:
            alco[0] = 1
        elif 10 <= alco[1] <= 50:
            alco[0] = 1.25
        elif 50 <= alco[1] <= 100:
            alco[0] = 1.5
        bot.send_message(call.message.chat.id, "пиво куплено и выпито")

    elif call.data == "mahitoby":
        alco[1] += 10
        maney -= 1000
        if 1 <= alco[1] <= 10:
            alco[0] = 1
        elif 10 <= alco[1] <= 50:
            alco[0] = 1.25
        elif 50 <= alco[1] <= 100:
            alco[0] = 1.5
        bot.send_message(call.message.chat.id, "махито куплен и выпит")

    elif call.data == "elby":
        alco[1] += 7.5
        maney -= 800
        if 1 <= alco[1] <= 10:
            alco[0] = 1
        elif 10 <= alco[1] <= 50:
            alco[0] = 1.25
        elif 50 <= alco[1] <= 100:
            alco[0] = 1.5
        bot.send_message(call.message.chat.id, "эль куплен и выпит")

    elif call.data == "wineby":
        alco[1] += 3
        maney -= 400
        if 1 <= alco[1] <= 10:
            alco[0] = 1
        elif 10 <= alco[1] <= 50:
            alco[0] = 1.25
        elif 50 <= alco[1] <= 100:
            alco[0] = 1.5
        bot.send_message(call.message.chat.id, "вино куплено и выпито")

    elif call.data == "homebt":
        listbt.tov = ["⚓.", "💧", "🐟", "🌊", "home", "baykalby", "amazonkaby", "okeanby", "locdalshe"]
        listbt.text = "⚓ Дом. Бесплатно.\n💧 Байкал 250.000\n🐟 Амазонка 750.000\n🌊 Ирландский океан 2.500.000"
        listbt.a(call.message)

    elif call.data == "baykalby":
        locals = ["ай мишаня Байкал", "Байкальский осётр", "Голомянка", "Омуль", 6, 5, 4]
        bot.send_message(call.message.chat.id, "Вы можете рыбачить на Байкале! +100 социал кредит и кошка жена")

    elif call.data == "amazonkaby":
        locals = ["Амазонка", "Электрический угорь", "Рыба-волк", "Пираньи", 8, 7, 6]
        bot.send_message(call.message.chat.id, "Вы приехали в БРАЗИЛ(иу) не умрите на Амазонке там очень опасно")

    elif call.data == "okeanby":
        locals = ["Ирландский океан", "Морской угорь", "Хек", "Мерланг", 10, 9, 8]
        bot.send_message(call.message.chat.id, "В\nС\nЁ")

#базы данных
@bot.message_handler(commands=["start"])
def start(message):
    global name
    name = message.from_user.username

    with sqlite3.connect("database.sql") as database:
        cur = database.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, maney INTEGER, frod VARCHAR(50), ex INTEGER, bait INTEGER, name VARCHAR(50))")
    
        cur.execute("SELECT * FROM users WHERE name = ?", (name,))
        existing_user = cur.fetchone()

        if not existing_user:
            cur.execute("INSERT INTO users (maney, frod, ex, bait, name) VALUES (?, ?, ?, ?, ?)", (maney, frod, ex, bait, name))
            database.commit()
            bot.send_message(message.chat.id, f"Добро пожаловать, {name}!")
        else:
            bot.send_message(message.chat.id, f"С возвращением, {name}!")

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
