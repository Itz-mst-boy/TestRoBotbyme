from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


devu = Client(
    "devu",
    api_id=8884119,
    api_hash="d94fe90a1d7ee5ce6f36b20d4ca79280",
    bot_token='5270362290:AAGIFRLpINGZX-v-CKOdlD-WV1X2g677f7g',
)

BUTTON = [
    [
      InlineKeyboardButton(text="Go in my Pm.", url='https://t.me/Banxinbot?start'),
    ],
]

@devu.on_message(filters.command('start') & filters.group)
def starcmd(devu, message):
	message.reply_text("Hey Use me in my pm Go here 👇", reply_markup=InlineKeyboardMarkup(BUTTON))



@devu.on_message(filters.command('start') & filters.private)
def command1(devu, message):
	devu.delete_messages(message.chat.id, message.id)	
	message.reply_text(f"Hello [{message.from_user.first_name}](tg://user?id={message.from_user.id}) 🥀\n\n I am basic info searcher bot made by `Mukesh`.\n\nType /getme to get your Info 🥀 \n\n Thank You ❤️")
	
		
@devu.on_message(filters.command('help'))
def help(devu, message):
	message.reply_text("Huh @trygoogle")	

BUTTUN = [
    [
      ("UserID"),
      ("UserInfo"),
    ],
]


@devu.on_message(filters.command('getme') & filters.private)
def info(devu, message):
	devu.delete_messages(message.chat.id, message.id)
	message.reply_text('Ok Choose What You Want To Know About YourSelf 👇.', reply_markup=ReplyKeyboardMarkup(BUTTUN, one_time_keyboard=True, resize_keyboard=True))
	

	
@devu.on_message(filters.regex('UserID') & filters.private)
def getuserid(devu, message):
	devu.delete_messages(message.chat.id, message.id)
	message.reply_text(f'Hey {message.from_user.first_name}\n\nYour Telegram UserID is `{message.from_user.id}`')
	
@devu.on_message(filters.regex('UserInfo') & filters.private)
def userinfo(devu, message):
	devu.delete_messages(message.chat.id, message.id)
	message.reply_text(f"""┈┈┈┈┈┈┈┈┈𑁍ࠬ┈┈┈┈┈
Scanned By Telegram Detabase..

User Info 🥀

First Name : `{message.from_user.first_name}`

Last Name : `{message.from_user.last_name}`

User ID : `{message.from_user.id}`

UserName : @{message.from_user.username}

Direct Link : [Link⚡](tg://user?id={message.from_user.id})

Enjoy!!
┈┈┈┈┈𑁍ࠬ┈┈┈┈┈┈┈┈""")

	
	


print("""╭┈┈┈┈┈┈┈𑁍ࠬ┈┈┈╮

❝ ᴍᴜᴋᴇsʜ ʀᴏʙᴏᴛ💝 ᴇɴɢᴀᴢᴇ ⚡ ❞

╰┈┈┈𑁍ࠬ┈┈┈┈┈┈┈╯""")
print("ᴏᴡɴᴇʀ🥀\n  ┗➤@itz_mst_boy")

devu.run()
