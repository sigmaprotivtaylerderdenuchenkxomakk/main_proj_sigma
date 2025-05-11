import requests
import telebot
import config
import top_dictd as td
import keyboardd as kb
import db_create as dc
from sqlite3 import *


dc.creare_db()

API = "0769adfc5718f7c971068946"
TOKEN = "7955185006:AAGUu8tpE0MX9RrkVhqycnaD9Iap-Dm1ru0"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    con = connect("users.db")
    sqll = """





"""
    sql = con.execute(
    """
    INSERT INTO user_data (user_id, chat_id) 
      VALUES(?,?)

  """, [message.from_user.id, message.chat.id]
)
    con.commit()
    if message.from_user.id in config.admins:
        bot.send_message(message.chat.id, "Выбери роль", reply_markup=kb.keyboard_admin)
    else:
        bot.send_message(message.chat.id, "Выберите валюту из которой будете переводить", reply_markup=kb.get_currency_keyboard1())

@bot.callback_query_handler(func=lambda call: "user" in call.data)
def handle_check_user(call: telebot.types.CallbackQuery):
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, "Выберите валюту из которой будете переводить", reply_markup=kb.get_currency_keyboard1())

@bot.callback_query_handler(func=lambda call: "admin" in call.data)
def handle_check_admin(call: telebot.types.CallbackQuery):
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, "Выберите действие:", reply_markup=kb.keyboard_admin_ad_post)

@bot.callback_query_handler(func=lambda call: "post" in call.data)
def handle_create_post(call: telebot.types.CallbackQuery):
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, f"Введите рекламу")
    bot.register_next_step_handler(call.message, handle_create_advert)
    
def handle_create_advert(message):
    pass


state = {}
        

@bot.callback_query_handler(func=lambda call: "currency" in call.data)
def handle_get_count_of_value(call: telebot.types.CallbackQuery):

    if "page" in call.data:
        _, _, page = call.data.split("_")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=kb.get_currency_keyboard1(int(page)))
        return

    _, code, name = call.data.split("_")
    state.update({call.from_user.id: code})
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, f"В какую валюту нужно перевести {td.top_currencies[code]}?", reply_markup=kb.get_currency_keyboard1_translate())
    

@bot.callback_query_handler(func=lambda call: "translate" in call.data)
def handle_get_count_of_value(call: telebot.types.CallbackQuery):
    if "page" in call.data:
        _, _, page = call.data.split("_")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=kb.get_currency_keyboard1_translate(int(page)))
        return
        
    _, code, name = call.data.split("_")
    firstcode = state.get(call.from_user.id)
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, f"Введите число которое нужно перевести из {td.top_currencies[firstcode]} в {td.top_currencies[code]}")   
    bot.register_next_step_handler(call.message, how_many, firstcode=firstcode, secondcode=code)


def how_many(message, firstcode, secondcode):
    try:
        count = message.text.strip()
        
    except AttributeError as e:
        bot.send_message(message.chat.id, f"Число!!!!!!!")
        bot.register_next_step_handler(message, how_many, firstcode=firstcode, secondcode=secondcode)
        return
    try:
        count = float(count)
    except ValueError as e:
        bot.send_message(message.chat.id, f"Число!!!!!!!")
        bot.register_next_step_handler(message, how_many, firstcode=firstcode, secondcode=secondcode)
        return



    try:
        if str(count)[0] == "0":
            if not len(str(count)) > 5:
                response = requests.get(f"https://v6.exchangerate-api.com/v6/{API}/pair/{firstcode}/{secondcode}")
                data = response.json()
                print(data)
                bot.send_message(message.chat.id,f"{count} {td.top_currencies[firstcode]} равно {data["conversion_rate"]*count} {td.top_currencies[secondcode]}")
            else:
                bot.send_message(message.chat.id, f"Число!!!!!!! по меньше плис")
                bot.register_next_step_handler(message, how_many, firstcode=firstcode, secondcode=secondcode)
        else:
            if not len(str(count)) > 100:
                response = requests.get(f"https://v6.exchangerate-api.com/v6/{API}/pair/{firstcode}/{secondcode}")
                data = response.json()
                print(data)
                bot.send_message(message.chat.id,f"{count} {td.top_currencies[firstcode]} равно {data["conversion_rate"]*count} {td.top_currencies[secondcode]}")
            else:
                bot.send_message(message.chat.id, f"Число!!!!!!! по меньше плис")
                bot.register_next_step_handler(message, how_many, firstcode=firstcode, secondcode=secondcode)
    except OverflowError as e:
        bot.send_message(message.chat.id, f"Число!!!!!!! по меньше плис")
        bot.register_next_step_handler(message, how_many, firstcode=firstcode, secondcode=secondcode)
        return
    except  telebot.apihelper.ApiTelegramException as e:
        pass
    
    


    



bot.polling(non_stop=True, interval=1)

# Делаем GET-запрос к API