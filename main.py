import telebot

TOKEN = "7871752923:AAFpNYXOdGFzIR-QYmjuQr3wtp49cO8UuwM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بيك، البوت شغال 🔥")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"قلت: {message.text}")

bot.infinity_polling()
