import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup

bot = telebot.TeleBot("7594349419:AAE1Lk-D5fqTu5jFUsZKj8nYnqpRiv71Wg0")

#start
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()

    reklama_button = types.InlineKeyboardButton("Реклама📄", callback_data="reklama")
    markup.row(reklama_button)

    bust_button = types.InlineKeyboardButton("Буст🏆", callback_data="bust")
    prokachka_button = types.InlineKeyboardButton("Прокачка🔝", callback_data="prokachka")
    markup.row(bust_button, prokachka_button)

    otzivi_button = types.InlineKeyboardButton("Отзывы📝", url="https://t.me/hunter_1508")
    help_button = types.InlineKeyboardButton("Помощь🆘", callback_data="help")
    markup.row(otzivi_button, help_button)

    bot.send_message(message.chat.id, f"Hello, <b>{message.from_user.first_name}</b> 😃", parse_mode="html", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def first_message(callback):

    markup2 = types.InlineKeyboardMarkup()

    buy_button = types.InlineKeyboardButton("Купить💵", url="https://t.me/hunter_1508")
    markup2.row(buy_button)

    exit_button = types.InlineKeyboardButton("Назад🔙", callback_data="exit")
    markup2.row(exit_button)

    markup3 =  types.InlineKeyboardMarkup()

    kirill_help = types.InlineKeyboardButton("Покупкой💳", url="https://t.me/hunter_1508")
    help_withbot = types.InlineKeyboardButton("Ботом🤖", url="https://t.me/zeevvaa")

    markup3.row(kirill_help, help_withbot,)

    markup3.row(exit_button)

    if callback.data == "reklama":
        bot.edit_message_text("<b><u>📄Реклама</u></b>:\n⭐️15 звезд - рекламный пост на <b>1,5 часа</b>\n⭐️25 звёзд - рекламный пост на <b>3 часа</b>\n⭐️40 звёзд - рекламный пост на <b>день</b>\n⭐️55 звёзд - рекламный пост на <b>два дня</b>\n⭐️150 звёзд - рекламный пост <b>навсегда</b>\n<b>Отзывы: @cabinReviews</b>", callback.message.chat.id, callback.message.message_id, reply_markup=markup2, parse_mode="html")

    elif callback.data == "bust":
        bot.edit_message_text("<b><u>🏆Буст</u></b>:\nБуст зависит от <b>бойца</b>, точнее на <b>каком месте в мете он находится</b>, по-этому сначала советуем посмотреть <b>актуальный список меты</b>.\n\n<b>Если у бойца 5 ⭐️</b>\n<b>⭐️10 звёзд</b> - 5 рангов ( боец полностью прокачен )\n<b>⭐️15 звёзд</b> - 5 рангов ( боец не полностью прокачен )\n<b>⭐️20 звёзд</b> - 5 рангов ( боец не прокачан )\n\nЕсли у бойца на <b>1 ⭐️ меньше</b>, то к сумме вы добавляете <b>+5 звёзд⭐️</b>.", callback.message.chat.id, callback.message.message_id, reply_markup=markup2, parse_mode="html")

    elif callback.data == "prokachka":
        bot.edit_message_text("<b><u>🔝Прокачка:</u></b>:\n<b>1 боец</b>:\n<b>⭐️70 звёзд</b> - LvL 0 🔜 LvL 11\n<b>⭐️150 звёзд</b> - LvL 0 🔜 LvL 11 + гаджеты, пасивки, гиперзаряд\n\n<b>X бойца(-цов)</b>:\n<b>⭐️70 звёзд ✖️ бойцы</b> - ( LvL 0 🔜 LvL 11 )\n<b>⭐️150 звёзд ✖️ бойцы</b> - ( LvL 0 🔜 LvL 11 + гаджеты, пасивки, гиперзаряд )", callback.message.chat.id, callback.message.message_id, reply_markup=markup2, parse_mode="html")

    elif callback.data == "help":
        bot.edit_message_text( "<b>Помощь c:</b>", callback.message.chat.id, callback.message.message_id, reply_markup=markup3, parse_mode="html")

    elif callback.data == "exit":
        bot.edit_message_text("<b>Напишите /start</b>", callback.message.chat.id, callback.message.message_id,
                              parse_mode="html")




bot.polling(none_stop=True)