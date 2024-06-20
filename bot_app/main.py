import telebot

bot = telebot.TeleBot(token= "7351679837:AAG6boVDRo0dI57BSTKq4vl28XhHgly8l74")

get_users = telebot.types.InlineKeyboardButton(text='GET USERS', callback_data='get_users')

keyboard = telebot.types.InlineKeyboardMarkup(keyboard=[[get_users]])

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id = message.chat.id, text = '<b>Привіт, користувач                         ᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠᅠ       </b>', reply_markup = keyboard, parse_mode='html')




bot.infinity_polling()

