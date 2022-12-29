import telebot

def send_notify(messege):
    bot = telebot.TeleBot('')
    bot.send_message('', messege)