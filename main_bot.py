'''
this code by yeuda by https://t.me/m100achuz


pip install Pyrogram
https://github.com/pyrogram/pyrogram.git
'''

from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#change this to your app_id and app_key from https://my.telegram.org/auth
app_id = 000000
app_key = '#########################'

#change this to your Token from https://t.me/BotFhater
token = "123456abcdefghijklmnopqrstzw"

app = Client("remove", app_id, app_key, bot_token=token)


TEXT_STARTED = 'The robot starts by removing {} users from the group'
TEXT_FINISH = 'The robot has finished removing {} users from the group'
TEXT_ERROR = 'Something failed. Check if I have received sufficient management permissions, or send it to the developer:\n {}'
TEXT_PRIVATE = '''
Hey, I'm a robot that will help you remove all users from your group

Add me to the group, and don't forget to give me proper management so I can remove them. Did you add them? Excellent. Now תשלחו בגעצון /kick and I am אתחיל in my work.

הروبوت نصر ع"ي [מכליד טידים] (tg://user?id=789248230). You can contact me for any request or comment, and I will try to help.
'''

status_admin = ["administrator", "creator"]
members_count_kicks = 0


@app.on_message(filters.group & filters.command("kick"))
def main(c,m):
    chat = m.chat
    global members_count_kicks
    status_member = chat.get_member(m.from_user.id)
    status_me = chat.get_member("me")
    if status_me.status == "administrator" and status_member in status_admin:
        try:
            members_count = str(chat.members_count)
            c.send_message(chat.id,TEXT_STARTED.format(members_count))
            for member in c.iter_chat_members(chat.id):
                if member.status in status_admin:
                    pass
                else:
                    chat.kick_member(member.user.id)
                    members_count_kicks += 1
            c.send_message(chat.id, TEXT_FINISH.format(members_count_kicks))
        except Exception as e:
            c.send_message(chat.id,TEXT_ERROR.format(str(e)))
    else:
        c.send_message(chat.id,TEXT_ERROR.format("no admin"))


@app.on_message(filters.group & filters.service)
def service(c,m):
    m.delete()

@app.on_message(filters.private)
def start(c,m):
    m.reply(TEXT_PRIVATE,disable_web_page_preview=True,reply_markup=InlineKeyboardMarkup(
          [[InlineKeyboardButton(text="My channel 🎀",
                       url="https://t.me/m100achuzyou")],
           [InlineKeyboardButton(text="עדכוני רובוטים",
                       url="https://t.me/M100achuzBots")]
           ]))


app.run()
