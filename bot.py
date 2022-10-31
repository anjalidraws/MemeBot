import telebot
import requests
bot = telebot.TeleBot("bot_token")

@bot.message_handler(commands=["meme"])
def meme(message):
    api_url = "https://meme-api.herokuapp.com/gimme"
    response = requests.get(api_url).json()
    bot.send_photo(message.chat.id, response["url"])

bot.polling()
