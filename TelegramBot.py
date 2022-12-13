from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token='')
updater = Updater(token='')
dispahather = updater.dispatcher


A = 0
B = 1

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите ваше предложение: ")
    return A

def find_and_delete(string):
    array = [x for x in string.split(" ") if "abc" not in x]
    new_string = " ".join(array)
    return new_string

def delete(update, context):
    text = update.message.text
    if "abc" in text.lower():
        my_string = find_and_delete(text)
        context.bot.send_message(update.effective_chat.id, my_string)
    return B

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, "Прощай")
    return ConversationHandler.END


cancel_handler = CommandHandler("cancel", cancel)
startHandler = CommandHandler("start", start)
deleteHandler = MessageHandler(Filters.text, delete)
conv_handler = ConversationHandler(entry_points=[startHandler],
                                   states={A: [deleteHandler],
                                           B: [cancel_handler]},
                                   fallbacks=[cancel_handler])


dispahather.add_handler(conv_handler)
dispahather.add_handler(cancel_handler)
dispahather.add_handler(startHandler)
dispahather.add_handler(deleteHandler)


updater.start_polling()
updater.idle()