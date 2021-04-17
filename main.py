"""
t.me/AmandaS2_bot
"""
import logging

import telegram.constants
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler,
                          CallbackContext)

apresentacao = 0
rodando = 1
conhece = 'sim'
n_conhece = 'não'


def start(update, context):
    msgs = ['Olá, eu sou o bot da Amanda! 😘✌️', 'Ela é uma pricesa 🧖']
    for msg in msgs:
        context.bot.send_message(update.effective_chat.id, msg)
    gif_princ = 'https://media.giphy.com/media/hWd7EG7YIfRni/giphy.gif'
    context.bot.send_animation(update.effective_chat.id, gif_princ)
    keyboard = [
        [
            InlineKeyboardButton("Sim 😍", callback_data=conhece),
            InlineKeyboardButton("Não 😒", callback_data=n_conhece),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(update.effective_chat.id, 'Você sabia disso? 🤔🤔🤔', reply_markup=reply_markup)
    return apresentacao


def comandos(update, context):
    chatid = update.effective_chat.id
    context.bot.send_message(chatid, 'Tente usar um dos comnandos:')
    lista_comandos = [
        '/comandos - Apresenta esta mensagem',
        '/start - Mensagem inicial',
        '/sobre - O que é este Bot',
        '/horoscopo - Apresenta o seu horoscopo do dia',
        '/vozinha - Vai te imitar com voizinha']
    comandos = '\n'.join(lista_comandos)
    context.bot.send_message(chatid, comandos)


def horoscopo(update, context):
    gif_horoscopo = 'https://media.giphy.com/media/THUFllpYw5hbSXvs19/giphy.gif'
    context.bot.send_animation(chat_id=update.effective_chat.id, animation=gif_horoscopo, caption='Vamos lá!')
    keyboard = [
        [
            InlineKeyboardButton("Sim ♓️", callback_data=conhece),
            InlineKeyboardButton('Não 👽', callback_data=n_conhece)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Tem certeza que deseja continuar?',
                             reply_markup=reply_markup)
    return apresentacao


def sim(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text('Ahh bom! Então sabe que ela é fodona.✌️')


def nao(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text('QUEEEEEEEEEEEEE?')
    msgs = ['COMO QUE NÃO CONHECE??', 'Vou tentar te ajudar com esse seu erro',
            'A Amanda é uma princesa, ela é linda, *U N I V E R S I T Á R I A*, além de ser muito inteligente,'
            ' trabalhadora, educada, com bom gosto e de peixe\. 😍 ']
    for msg in msgs:
        query.bot.send_message(update.effective_chat.id, msg, parse_mode=telegram.constants.PARSEMODE_MARKDOWN_V2)


def ctz(update, context):
    query = update.callback_query
    query.answer()
    gif = 'https://media.giphy.com/media/AjYsTtVxEEBPO/giphy.gif'
    query.bot.send_animation(chat_id=update.effective_chat.id, animation=gif,
                             caption= 'PARE DE LOUCURA, ISSO *NÃO* EXISTE\!\!\!\n👺👺👺👺👺👺👺👺👺',
                             parse_mode=telegram.constants.PARSEMODE_MARKDOWN_V2
                             )


def n_ctz(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text('Ok. Fica para a próxima.\n♈️ ♉️ ♊️ ♋️ ♌️ ♍️ ♎️ ♏️ ♐️ ♑️ ♒️ ♓️')

# def send_gif(update, context):
#     gif_link = 'https://media.giphy.com/media/yFQ0ywscgobJK/giphy.gif'
#     context.bot.send_animation(chat_id=update.effective_chat.id, animation=gif_link)


def sobre(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Este bot foi feito para mostrar o quão incrível é'
                                                                    ' esta mulher, Amanda ❤️.')


def voizinha(update, context):
    pass


def main():
    file = open('token.txt')
    token = file.read()
    file.close()

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    conv_handler = ConversationHandler(entry_points=[CommandHandler('start', start)],
                                       states={
                                           apresentacao: [
                                               CallbackQueryHandler(sim, pattern='sim'),
                                               CallbackQueryHandler(nao, pattern='não')
                                           ],
                                           rodando: [

                                           ]
                                       },
                                       fallbacks=[CommandHandler('start', start)])
    horoscopo_handler = ConversationHandler(entry_points=[CommandHandler('horoscopo', horoscopo)],
                                            states={
                                                apresentacao: [
                                                    CallbackQueryHandler(ctz, pattern='sim'),
                                                    CallbackQueryHandler(n_ctz, pattern='não')
                                                ],
                                                rodando: [

                                                ]
                                            },
                                            fallbacks=[CommandHandler('horoscopo', horoscopo)])
    dispatcher.add_handler(conv_handler)
    # dispatcher.add_handler(CommandHandler('gif', send_gif))
    dispatcher.add_handler(CommandHandler('sobre', sobre))
    dispatcher.add_handler(horoscopo_handler)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, voizinha))
    dispatcher.add_handler(CommandHandler('comandos', comandos))

    # Start the bot
    updater.start_polling()
    # Para parar o bot depois de iniciado. Ctrl - C
    updater.idle()


if __name__ == '__main__':
    main()
