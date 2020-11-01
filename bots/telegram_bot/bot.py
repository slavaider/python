# pip install pytelegrambotapi
import datetime

import telebot

bot = telebot.TeleBot('1435231643:AAEL7qWiyJpuU8QB5c3XUeySTRAImWoJsXg')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Время', 'Погода')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, message.text)
    if message.text.lower() == 'время':
        now = datetime.datetime.now().strftime("%H:%M:%S")
        bot.send_message(message.chat.id, f'Привет, мой создатель, сегодня {now}')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


if __name__ == '__main__':
    bot.infinity_polling()
