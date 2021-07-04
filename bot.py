from main import getShopCategories, categoryPrice
from config import telebotAPI, shopList
import telebot


# cd venv/Scripts/
# activate.bat  
bot = telebot.TeleBot(telebotAPI)
shopsKeyBoard = telebot.types.ReplyKeyboardMarkup()
helpKeyBoard = telebot.types.ReplyKeyboardMarkup()
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard3 = telebot.types.ReplyKeyboardMarkup()

for shop in shopList:
    shopsKeyBoard.add(shop)

helpKeyBoard.row()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Привет, я помогу тебе отыскать скидки, которые тебе надо 😎\nВыбери магазин, который тебя интересует.', reply_markup=shopsKeyBoard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(
        message.chat.id, 'Хелп текст', reply_markup=helpKeyBoard)


@bot.message_handler(content_types=['text'])
def getShopName(message):
    global shopCategories
    if message.text in shopList:
        shopCategories = getShopCategories(message.text)
        for category in shopCategories:
            keyboard2.add(category)
        bot.send_message(message.chat.id, f'Выберите категорию', reply_markup=keyboard2)
        bot.register_next_step_handler(message, getCategoryPrice)
    else:
        bot.send_message(message.chat.id, f'Выбери магазин, который тебя интересует из списка', reply_markup=shopsKeyBoard)




def getCategoryPrice(message):
    bot.send_message(message.chat.id, f'Скидки на продукты в категории {message.text} такие:\n{categoryPrice(message.text)}')
        # bot.register_next_step_handler(message, getDiscounts)
        

# def getDiscounts(message):
    


bot.polling()