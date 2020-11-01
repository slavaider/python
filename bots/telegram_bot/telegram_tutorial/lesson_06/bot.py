#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import random

import telebot
from lesson_06 import botan
from lesson_06 import config

bot = telebot.TeleBot(config.token)
random.seed()


@bot.message_handler(commands=['random'])
def cmd_random(message):
    bot.send_message(message.chat.id, random.randint(1, 10))
    # Если не нужно собирать ничего, кроме количества использований, замените третий аргумент message на None
    botan.track(config.botan_key, message.chat.id, message, 'Случайное число')


@bot.message_handler(commands=['yesorno'])
def cmd_yesorno(message):
    bot.send_message(message.chat.id, random.choice(strings))
    # Если не нужно собирать ничего, кроме количества использований, замените третий аргумент message на None
    botan.track(config.botan_key, message.chat.id, message, 'Да или нет')


if __name__ == '__main__':
    global strings
    strings = ['Да', 'Нет']
    bot.infinity_polling()
