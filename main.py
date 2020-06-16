import telebot
import os
from busInfo import get_bus_info, bus_info_to_string

"""
bot name: VanBusStopInfo
bot username: VanBusStopInfoBot
heroku: https://gentle-island-84337.herokuapp.com/ | https://git.heroku.com/gentle-island-84337.git
"""

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help', 'start'])
def help_handler(message):
    text = """
    Works in Vancouver, BC area only
    Author Haim Fridland 
    hfridland@shaw.ca
    /start, /help - for obtaining info about nearest bus stops please enter current location
    """
    bot.send_message(chat_id=message.chat.id, text=text)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    lat = message.location.latitude
    lon = message.location.longitude
    s = bus_info_to_string(get_bus_info(lat, lon))

    bot.send_message(chat_id=message.chat.id, text="Bus stops:\n" + s)


bot.polling()
