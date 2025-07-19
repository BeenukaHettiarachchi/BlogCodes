from pyrogram import Client, filters


bot = Client(
    name='examplebot',           # pass whatever name (bot name, your name, etc)
    api_id=12345,                # pass your API_ID (as a int or str)
    api_hash='your api hash',    # pass your API_HASH (as a str)
    bot_token='your bot token'   # pass your BOT_TOKEN (as a str)
)


@bot.on_message(filters.new_chat_members)
def welcome(client, message):
    message.reply('Hi, welcome to the chat!')

bot.run()