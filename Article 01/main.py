from pyrogram import Client


bot = Client(
    name='examplebot',           # pass whatever name (bot name, your name, etc)
    api_id=12345,                # pass your API_ID (as a int or str)
    api_hash='your api hash',    # pass your API_HASH (as a str)
    bot_token='your bot token'   # pass your BOT_TOKEN (as a str)
)


@bot.on_message()
def echo(client,message):
    text = message.text
    message.reply(text)

bot.run()