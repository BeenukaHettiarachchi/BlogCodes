from pyrogram import Client, filters

bot = Client(
    name='examplebot',           
    api_id=12345,                
    api_hash='your api hash',    
    bot_token='your bot token'   
)


@bot.on_message(filters.command('start') & filters.private)
def love(client, message):
    chat_id = message.chat.id
    client.send_message(
        chat_id=chat_id,
        text='Do you like me?'
    )

bot.run()