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
    firstname = message.from_user.first_name
    user_id = message.from_user.id
    username = message.from_user.username
    datetime = message.date
    
    custom_reply = (
        f'**Name:** {firstname}\n',
        f'**ID:** {user_id}\n',
        f'**Username**: {username}\n',
        f'**Text:** {text}\n',
        f'**Date & Time:** {datetime}'
    )
    message.reply(custom_reply)

bot.run()