import telebot
from busInfo import get_bus_info, bus_info_to_string

"""
bot name: VanBusStopInfo
bot username: VanBusStopInfoBot
heroku: https://bot-bus.herokuapp.com/ | https://git.heroku.com/bot-bus.git
        https://sheltered-harbor-89619.herokuapp.com/ | https://git.heroku.com/sheltered-harbor-89619.git
"""

token = '1115434264:AAHSsZqEB-WF52QekjnnSjyv_dd6MDjhqlA'
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
    # print(message.location)
    lat = message.location.latitude
    lon = message.location.longitude
    s = bus_info_to_string(get_bus_info(lat, lon))

    bot.send_message(chat_id=message.chat.id, text="Bus stops:\n" + s)


bot.polling()
