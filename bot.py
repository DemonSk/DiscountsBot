from main import func
from config import telebotAPI
import telebot


# cd venv/Scripts/
# activate.bat  
bot = telebot.TeleBot(telebotAPI)
keyboard1 = telebot.types.ReplyKeyboardMarkup()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Привет, я помогу тебе отыскать скидки, которые тебе надо 😎', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'скидки':
        bot.send_message(message.chat.id, f'Скидки на продукты такие:\n{func()}')
    elif message.text.lower() == 'end':
        bot.send_message(message.chat.id, 'Good bye')


bot.polling()