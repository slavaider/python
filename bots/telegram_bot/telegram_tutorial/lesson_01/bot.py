# -*- coding: utf-8 -*-

import telebot

token = '1435231643:AAEL7qWiyJpuU8QB5c3XUeySTRAImWoJsXg'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, важно не повторяться
    bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
