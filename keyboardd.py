
import telebot
import top_dictd as td


def get_currency_keyboard1(page=1):
    keyboard1 = telebot.types.InlineKeyboardMarkup(row_width=3)
    next_button1 = telebot.types.InlineKeyboardButton(text=f"Перейти на {page%2+1} стр", callback_data=f"currency_page_{page%2+1}")
    buttons = []
    for code, name in list(td.top_currencies.items())[(page-1)*30:page*30]:
        buttons.append(telebot.types.InlineKeyboardButton(text=f"{code} - {name}", callback_data=f"currency_{code}_{name}"))
    keyboard1.add(*buttons)
    keyboard1.add(next_button1)
    return keyboard1

def get_currency_keyboard2():
    keyboard2 = telebot.types.InlineKeyboardMarkup(row_width=3)
    next_button2 = telebot.types.InlineKeyboardButton(text=f"Перейти на 3 стр", callback_data="next2")
    back_button2 = telebot.types.InlineKeyboardButton(text=f"Перейти на 1 стр", callback_data="back2")
    buttons = []
    for code, name in list(td.top_currencies.items())[30:67]:
        buttons.append(telebot.types.InlineKeyboardButton(text=f"{code} - {name}", callback_data=f"currency_{code}_{name}"))
    keyboard2.add(*buttons)
    keyboard2.add(next_button2)
    keyboard2.add(back_button2)
    return keyboard2

def get_currency_keyboard3():
    keyboard3 = telebot.types.InlineKeyboardMarkup(row_width=3)
    back_button3 = telebot.types.InlineKeyboardButton(text=f"Перейти на 2 стр", callback_data="back3")
    buttons = []
    for code, name in list(td.top_currencies.items())[67:96]:
        buttons.append(telebot.types.InlineKeyboardButton(text=f"{code} - {name}", callback_data=f"currency_{code}_{name}"))
    keyboard3.add(*buttons)
    keyboard3.add(back_button3)
    return keyboard3



def get_currency_keyboard1_translate(page=1):
    keyboard1 = telebot.types.InlineKeyboardMarkup(row_width=3)
    next_button1 = telebot.types.InlineKeyboardButton(text=f"Перейти на {page%2+1} стр", callback_data=f"translate_page_{page%2+1}")
    buttons = []
    for code, name in list(td.top_currencies.items())[(page-1)*30:page*30]:
        buttons.append(telebot.types.InlineKeyboardButton(text=f"{code} - {name}", callback_data=f"translate_{code}_{name}"))
    keyboard1.add(*buttons)
    keyboard1.add(next_button1)
    return keyboard1

def get_currency_keyboard2_translate():
    keyboard2 = telebot.types.InlineKeyboardMarkup(row_width=3)
    next_button2 = telebot.types.InlineKeyboardButton(text=f"Перейти на 3 стр", callback_data="next2")
    back_button2 = telebot.types.InlineKeyboardButton(text=f"Перейти на 1 стр", callback_data="back2")
    buttons = []
    for code, name in list(td.top_currencies.items())[30:67]:
        buttons.append(telebot.types.InlineKeyboardButton(text=f"{code} - {name}", callback_data=f"translate_{code}_{name}"))
    keyboard2.add(*buttons)
    keyboard2.add(next_button2)
    keyboard2.add(back_button2)
    return keyboard2

def get_currency_keyboard3_translate():
    keyboard3 = telebot.types.InlineKeyboardMarkup(row_width=3)
    back_button3 = telebot.types.InlineKeyboardButton(text=f"Перейти на 2 стр", callback_data="back3")
    buttons = []
    for code, name in list(td.top_currencies.items())[67:96]:
        buttons.append(telebot.types.InlineKeyboardButton(text=f"{code} - {name}", callback_data=f"translate_{code}_{name}"))
    keyboard3.add(*buttons)
    keyboard3.add(back_button3)
    return keyboard3



keyboard_admin = telebot.types.InlineKeyboardMarkup(row_width=1)
button_admin = telebot.types.InlineKeyboardButton(text=f"Админ", callback_data="admin")
button_user = telebot.types.InlineKeyboardButton(text=f"Пользователь", callback_data="user")
keyboard_admin.add(button_admin)
keyboard_admin.add(button_user)


keyboard_admin_ad_post = telebot.types.InlineKeyboardMarkup(row_width=1)
button_create_ad = telebot.types.InlineKeyboardButton(text=f"Создать пост/рекламу", callback_data="create")
button_be_user = telebot.types.InlineKeyboardButton(text=f"Стать пользователем", callback_data="user")
button_delete_ad = telebot.types.InlineKeyboardButton(text=f"Удалить", callback_data="delete")
keyboard_admin_ad_post.add(button_create_ad)
keyboard_admin_ad_post.add(button_be_user)






