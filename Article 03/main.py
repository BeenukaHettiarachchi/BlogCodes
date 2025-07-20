from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Client(
    name='examplebot',           
    api_id=12345,                
    api_hash='your api hash',    
    bot_token='your bot token'   
)

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Yes😍',callback_data='yes'),
            InlineKeyboardButton('No😏',callback_data='no')
        ]
    ]
)


@bot.on_message(filters.command('start') & filters.private)
def love(client, message):
    chat_id = message.chat.id
    client.send_message(
        chat_id=chat_id,
        text='Do you like me?',
        reply_markup=keyboard
    )

@bot.on_callback_query()
def react(client, query):
    data = query.data
    message = query.message
    if data == 'yes':
        message.edit('I knew it😘')
    else:
        message.edit('Neither do I😏')

bot.run()