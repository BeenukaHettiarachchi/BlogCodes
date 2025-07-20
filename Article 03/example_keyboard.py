from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Client(
    name='examplebot',           
    api_id=12345,                
    api_hash='your api hash',    
    bot_token='your bot token'   
)


example_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('R1,C1',callback_data='r1c1'),
            InlineKeyboardButton('R1,C2',callback_data='r1c2'),
            InlineKeyboardButton('R1,C3',callback_data='r1c3')
        ],
        [
            InlineKeyboardButton('R2,C1',callback_data='r2c1'),
            InlineKeyboardButton('R2,C2',callback_data='r2c2'),
            InlineKeyboardButton('R2,C3',callback_data='r2c3')
        ],
        [
            InlineKeyboardButton('R3,C1',callback_data='r3c1'),
            InlineKeyboardButton('R3,C2',callback_data='r3c2')
        ]
    ]
)    

@bot.on_message(filters.command('example'))
def example_button(client, message):
    message.reply(
        text='Example Inline Keyboard',
        reply_markup=example_keyboard
    )


bot.run()   