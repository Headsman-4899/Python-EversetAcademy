import telebot

bot = telebot.TeleBot('5287295989:AAHnqgqMpX6WHf-lkDvmHVgjKvELTvC4gvE')


@bot.message_handler(commands=['start'])
def start(message):
    msg = "Hello, my name is BestCurrencyBot!" +  "\n" + "Write \"/kz\" command to get a link to check an actual currency of KZ." + "\n" + "Write \"/usd\" command to get a link to check an actual currency of USD." + "\n" + "Write \"/eur\" command to get a link to check an actual currency of EURO."
    bot.send_message(message.chat.id, msg, parse_mode='')


@bot.message_handler(commands='kz')
def get_user_text(message):
    kzUrl = "https://bhom.ru/currencies/kzt/?sb=yes&startdate=" + dtf.format(date.plusDays(-10)) + "&enddate=" + dtf.format(date);
    bot.send_message(message.chat.id, message, parse_mode='')


bot.polling(none_stop=True)
