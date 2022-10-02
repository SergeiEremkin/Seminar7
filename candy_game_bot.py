import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
CANDY_COUNT, PER_TURN , PLAYER_TURN, COMPUTER_TURN = range(4)

# функция обратного вызова точки входа в разговор
def start(update, _):
    update.message.reply_text(
        'Добро пожаловать в игру "Конфета". Цель игры, чтобы ваш противник взял последнюю конфету.\n'
        'Команда /cancel, чтобы прекратить разговор.\n\n')
    update.message.reply_text(
            'Введите кол-во конфет в куче: ')    
    return CANDY_COUNT


def candy_count(update, context):
    user = update.message.from_user
    logger.info("Кол-во конфет: %s: %s", user.first_name, update.message.text)
    candy_count = update.message.text
    if candy_count.isdigit():
        candy_count = int(candy_count)
        context.user_data['candy_count'] = candy_count
        update.message.reply_text(
            f'В куче {candy_count} конфет\n')
        update.message.reply_text(
            f'Введите кол-во конфет, которое можно забрать за ход.\n(Оно должно быть меньше общего колличества конфет в куче): ')  
        return PER_TURN
    else:
         update.message.reply_text(
            f'Вы ввели не число\n')
    

def per_turn(update, context):
    user = update.message.from_user
    logger.info("Кол-во конфет за ход %s: %s", user.first_name, update.message.text)
    candy_count = context.user_data.get('candy_count')
    turn_count = update.message.text
    if turn_count.isdigit():
        turn_count = int(turn_count)
        if candy_count > turn_count and turn_count > 0:
                context.user_data['turn_count'] = turn_count
                update.message.reply_text(
                    f'За ход можно брать от 1 до {turn_count} конфет\n')
                update.message.reply_text(
                f'Ваш ход. Введите число в диапазоне от 1 до {turn_count}: ')
                return PLAYER_TURN
        else:
               update.message.reply_text(f'Максимально допустимое значение {candy_count -1}') 
    else:
         update.message.reply_text(
            f'Вы ввели не число\n')
    


def player_turn(update, context):
    user = update.message.from_user
    logger.info(
        "Ход игрока %s: %f / %f", user.first_name, update.message.text)
    turn_count =context.user_data.get('turn_count')
    candy_count = context.user_data.get('candy_count')
    if candy_count < turn_count:
        turn_count = turn_count - (turn_count - candy_count)
    player_turn = update.message.text
    if player_turn.isdigit():
        player_turn = int(player_turn)
        if player_turn <= turn_count:
                candy_count -= player_turn
                if candy_count < 1:
                    update.message.reply_text(
                        f'Игрок проиграл') 
                    return ConversationHandler.END 
                context.user_data['candy_count'] = candy_count
                update.message.reply_text(
                        f'Вы ввели {player_turn} конфет. В куче осталось {candy_count}: ')
                update.message.reply_text(f'Внимание ходит бот...')
                context.user_data['turn_count']=turn_count             
                return COMPUTER_TURN
        else:
                update.message.reply_text(
                        f'Максимально допустимое значение за ход - {turn_count}')    
    else:
        update.message.reply_text(
                        f'Нужно ввести число')


        
def computer_turn(update, context):
    turn_count = context.user_data.get('turn_count')
    candy_count = context.user_data.get('candy_count')
    if candy_count < turn_count:
        turn_count = turn_count - (turn_count - candy_count)
    if candy_count > 1:
        candy_count -= turn_count-1
    else:
        candy_count -= turn_count
    if candy_count <1:
        update.message.reply_text(
                        f'Бот проиграл')
        return ConversationHandler.END 
    context.user_data['candy_count'] = candy_count
    update.message.reply_text(
            f'Бот походил на {turn_count-1} конфет. В куче осталось {candy_count}: ')
    update.message.reply_text(
            f'Ваш ход. Введите число в диапазоне от 1 до {turn_count}: ')
    context.user_data['turn_count']=turn_count            
    return PLAYER_TURN

    
    
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
    )
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    game_conversation_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CANDY_COUNT:[MessageHandler(Filters.text, candy_count)],
            PER_TURN: [MessageHandler(Filters.text, per_turn)],
            PLAYER_TURN:[MessageHandler(Filters.text, player_turn)],
            COMPUTER_TURN: [MessageHandler(Filters.text, computer_turn)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(game_conversation_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()