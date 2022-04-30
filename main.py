from pyrogram import Client, filters

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


devu = Client(
    "devu",
    api_id=8884119,
    api_hash="d94fe90a1d7ee5ce6f36b20d4ca79280",
    bot_token='5382418732:AAGSE1Ym7g7YT80OpqDft-QHZgTu0Oshdiw',
)

BUTTON = [
    [
      InlineKeyboardButton(text="ɢᴏ ɪɴ ᴍʏ ᴘᴍ.", url='https://t.me/MoI_inFo_bOt?start'),
    ],
]

@devu.on_message(filters.command('start') & filters.group)
def starcmd(devu, message):
	message.reply_text("ʜᴇʏ  ᴜsᴇ ᴍᴇ ɪɴ ᴍʏ ᴘᴍ ɢᴏ ʜᴇʀᴇ 👇", reply_markup=InlineKeyboardMarkup(BUTTON))



@devu.on_message(filters.command('start') & filters.private)
def command1(devu, message):
	devu.delete_messages(message.chat.id, message.id)	
	message.reply_text(f"ʜᴇʟʟᴏ[{message.from_user.first_name}](tg://user?id={message.from_user.id}) 🥀\n\n ɪ  ᴀᴍ  ʙᴀsɪᴄ ɪɴғᴏ sᴇᴀʀᴄʜᴇʀ ʙᴏᴛ ᴍᴀᴅᴇ  byǫ `ᴍᴜᴋᴇsʜ @itz_mst_boy`.\n\nᴛʏᴘᴇs /getme ᴛᴏ  ɢᴇᴛ ʏᴏᴜʀ  ɪɴғᴏ 🥀 \n\n ᴛʜᴀɴᴋ  ʏᴏᴜ  ᴘʟᴢ ᴊᴏɪɴ @mr_sukkun❤️")
	
		
@devu.on_message(filters.command('help'))
def help(devu, message):
	message.reply_text("ʜᴜʜ  ᴄᴏɴᴛᴀᴄᴛ @itz_mst_boy")	

BUTTUN = [
    [
      ("UserID"),
      ("UserInfo"),
    ],
]


@devu.on_message(filters.command('getme') & filters.private)
def info(devu, message):
	devu.delete_messages(message.chat.id, message.id)
	message.reply_text('ᴏᴋ ᴄʜᴏᴏsᴇ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ʏᴏᴜʀsᴇʟғ 👇.', reply_markup=ReplyKeyboardMarkup(BUTTUN, one_time_keyboard=True, resize_keyboard=True))
	

	
@devu.on_message(filters.regex('UserID') & filters.private)
def getuserid(devu, message):
	devu.delete_messages(message.chat.id, message.id)
	message.reply_text(f'ʜᴇʏ {message.from_user.first_name}\n\nʏᴏᴜʀ  ᴛᴇʟᴇɢʀᴀᴍ  ᴜsᴇʀɪᴅ ɪs  `{message.from_user.id}`')
	
@devu.on_message(filters.regex('UserInfo') & filters.private)
def userinfo(devu, message):
	devu.delete_messages(message.chat.id, message.id)
	message.reply_text(f"""┈┈┈┈┈┈┈┈┈𑁍ࠬ┈┈┈┈┈
sᴄᴀɴɴᴇᴅ ʙʏ ᴛᴇʟᴇɢʀᴀᴍ  ᴅᴀᴛᴀʙᴀsᴇ ᴍᴏɪ ᴏᴡɴᴇʀ @itz_mst_boy..

ᴜsᴇʀ  ɪɴғᴏ  🥀

ғɪʀsᴛ  ɴᴀᴍᴇ  : `{message.from_user.first_name}`

ʟᴀsᴛ ɴᴀᴍᴇ  : `{message.from_user.last_name}`

ᴜsᴇʀ ɪᴅ : `{message.from_user.id}`

ᴜsᴇʀɴᴀᴍᴇ : @{message.from_user.username}

ᴅɪʀᴇᴄᴛ ʟɪɴᴋ : [Link⚡](tg://user?id={message.from_user.id})

ᴇɴᴊᴏʏ  ʙʏ @itz_mst_boy 
 ᴊᴏɪɴ:- @mukhushi_official!!
┈┈┈┈┈𑁍ࠬ┈┈┈┈┈┈┈┈""")

	
	


print("""╭┈┈┈┈┈┈┈𑁍ࠬ┈┈┈╮

❝ ᴍᴜᴋᴇsʜ ʀᴏʙᴏᴛ💝 ᴇɴɢᴀᴢᴇ ⚡ ❞

╰┈┈┈𑁍ࠬ┈┈┈┈┈┈┈╯""")
print("ᴏᴡɴᴇʀ🥀\n  ┗➤@itz_mst_boy")

devu.run()
