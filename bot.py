import telebot
from telebot import types
import random

bot = telebot.TeleBot('7848048582:AAGok3ezwrSuHR7FB_0L32kw7i1XXpMjnMM')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Привет,это бот где ты можешь поиграть с шансами и выбить самую редкую карточку или просто пофармить монеты и стать самым лучшим')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Крути')
    keyboard.add(button)
    bot.reply_to(message,'Нажми на кнопку и крути',reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Крути')
def spin(message):
    roll =  random.random()
    if roll <= 0.0001:
        with open('pics/bomb.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f) 
            bot.reply_to(message,'Поздравляю вы выбили ядерку,удачи')
    elif roll <= 0.001:
        with open('pics/mythic.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif roll <= 0.01:
        with open('pics/legend.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif roll <= 0.08:
        with open('pics/epic.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif roll <= 0.25:
        with open('pics/rare.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif roll >= 0.5:
        with open('pics/common.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    print(roll)




bot.infinity_polling()