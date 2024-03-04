from bot_token import TOKEN
from weather import current_weather
import telebot
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["weather"])
def weather_command(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton("Поделиться местоположением", request_location=True)
    keyboard.add(button)
    bot.send_message(message.chat.id, "Поделитесь своим местоположением", reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def location_handler(message):
    weather = current_weather(message.location.latitude, message.location.longitude)
    keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     f"""Температура: {weather[0]}°C
Скорость ветра: {weather[1]} м/с
Направление ветра: {weather[2]}
Тип погоды: {weather[3]}""",
                     reply_markup=keyboard)


if __name__ == '__main__':
    bot.infinity_polling()
