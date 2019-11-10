import telebot

bot = telebot.TeleBot('966679592:AAHbIIpeRiqlt5cFIYBn1Ius_wME0lNPvSs')

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)

bot.polling(none_stop = True )  