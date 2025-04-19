import os, asyncio, humanize
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from bot import Bot
from config import ADMINS, FORCE_MSG, START_PIC, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT, FILE_AUTO_DELETE
from helper_func import *
from database.database import add_user, del_user, full_userbase, present_user, is_requested_one, is_requested_two, delete_all_one, delete_all_two, subscribed3, get_invite_link
from plugins.fsub import *

madflixofficials = FILE_AUTO_DELETE
jishudeveloper = madflixofficials
file_auto_delete = humanize.naturaldelta(jishudeveloper)




@Bot.on_message(filters.command('start') & filters.private & subscribed1 & subscribed2 & subscribed3 & subscribed4)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass
    text = message.text
    if len(text)>7:
        
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please Wait...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something Went Wrong..!")
            return
        await temp_msg.delete()
    
        madflix_msgs = [] # List to keep track of sent messages

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                madflix_msg = await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                # await asyncio.sleep(0.5)
                madflix_msgs.append(madflix_msg)
                
            except FloodWait as e:
                await asyncio.sleep(e.x)
                madflix_msg = await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                madflix_msgs.append(madflix_msg)
                
            except:
                pass


        k = await client.send_message(chat_id = message.from_user.id, text=f"<b>❗️ <u>𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗧</u> ❗️</b>\n\n<b>Tʜɪs Aɴɪᴍᴇ Fɪʟᴇ Wɪʟʟ Bᴇ Dᴇʟᴇᴛᴇᴅ Iɴ {file_auto_delete} (Dᴜᴇ Tᴏ Cᴏᴘʏʀɪɢʜᴛ Issᴜᴇs)</b>.\n\n<b>📌 Pʟᴇᴀsᴇ Fᴏʀᴡᴀʀᴅ Tʜɪs Aɴɪᴍᴇ Fɪʟᴇ Tᴏ Sᴏᴍᴇᴡʜᴇʀᴇ Eʟsᴇ Aɴᴅ Sᴛᴀʀᴛ Dᴏᴡɴʟᴏᴀᴅɪɴɢ Tʜᴇʀᴇ.</b>")

        # Schedule the file deletion
        asyncio.create_task(delete_files(madflix_msgs, client, k))
        
        # for madflix_msg in madflix_msgs: 
            # try:
                # await madflix_msg.delete()
                # await k.edit_text("Your Video / File Is Successfully Deleted ✅") 
            # except:    
                # pass 

        return
    else:
        reply_markup = InlineKeyboardMarkup([[
            InlineKeyboardButton("⚡𝙹𝚘𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕s⚡', url=f'https://t.me/addlist/VjgALaxe725mZjY1"),
            InlineKeyboardButton("⚡Oᴜʀ Gʀᴏᴜᴘ⚡', url=f'https://t.me/+8bE6LN_37EBmNGNl")
            ],[
            InlineKeyboardButton("📢Help", callback_data="help"),
            InlineKeyboardButton("⚡About", callback_data="about")
            ],[
            InlineKeyboardButton("❌Close", callback_data="close")
        ]])
        await message.reply_photo(
            photo= START_PIC,
            caption= START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup
            
        )
        return

    


@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    invite_link = get_invite_link()
    buttons = []
    
    if client.link_one is not None and message.from_user.id not in ADMINS and not await is_requested_one(filter, client, message):
        buttons.append([InlineKeyboardButton("• Rᴇǫᴜᴇꜱᴛ Channel •", url=client.link_one)])
    # Check if the first and second channels are both set
    if client.invitelink is not None and message.from_user.id not in ADMINS and not await is_subscribed(filter, client, message):
        buttons.append([InlineKeyboardButton(text="• ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •", url=client.invitelink)])
            
    if client.invitelink1 is not None and message.from_user.id not in ADMINS and not await is_subscribed2(filter, client, message):
        buttons.append([InlineKeyboardButton(text="• ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •", url=client.invitelink1)])


    if invite_link is not None and message.from_user.id not in ADMINS and not await is_subscribed3(filter, client, message):
        buttons.append([InlineKeyboardButton(text="• ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •", url=invite_link)])
        
    try:
        buttons.append([
            InlineKeyboardButton(
                text="⚡ Get File ⚡",
                url=f"https://t.me/{client.username}?start={message.command[1]}"
            )
        ])
    except IndexError:
        pass  # Ignore if no second argument is present


    await client.send_photo(
                chat_id=message.from_user.id,
                photo= START_PIC,
                caption="**Please Join the Following Channels to use this Bot! 👇**",
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN
    )
    


@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=f"Processing...")
    users = await full_userbase()
    await msg.edit(f"{len(users)} Users Are Using This Bot")



@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                sent_msg=await broadcast_msg.copy(chat_id)
                successful += 1
                asyncio.create_task(delete_broadcast_messages(client, chat_id, sent_msg.id))
            except FloodWait as e:
                await asyncio.sleep(e.x)
                sent_msg=await broadcast_msg.copy(chat_id)
                successful += 1
                asyncio.create_task(delete_broadcast_messages(client, chat_id, sent_msg.id))
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u></b>

<b>Total Users :</b> <code>{total}</code>
<b>Successful :</b> <code>{successful}</code>
<b>Blocked Users :</b> <code>{blocked}</code>
<b>Deleted Accounts :</b> <code>{deleted}</code>
<b>Unsuccessful :</b> <code>{unsuccessful}</code>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(f"Use This Command As A Reply To Any Telegram Message With Out Any Spaces.")
        await asyncio.sleep(8)
        await msg.delete()






# Function to handle file deletion
async def delete_files(messages, client, k):
    await asyncio.sleep(FILE_AUTO_DELETE)  # Wait for the duration specified in config.py
    for msg in messages:
        try:
            await client.delete_messages(chat_id=msg.chat.id, message_ids=[msg.id])
        except Exception as e:
            print(f"The attempt to delete the media {msg.id} was unsuccessful: {e}")
    # await client.send_message(messages[0].chat.id, "Your Video / File Is Successfully Deleted ✅")
    await k.edit_text("Your Video / File Is Successfully Deleted ✅")

async def delete_broadcast_messages(client, chat_id, message_id):
    await asyncio.sleep(86400)  # Wait for the duration specified in config.py    
    try:
        await client.delete_messages(chat_id, message_id)
    except Exception as e:
        print(f"The attempt to delete the media was unsuccessful: {e}")
    



@Bot.on_message(filters.command('clear_req_1') & filters.private & filters.user(ADMINS))
async def purge_req_one(bot, message):
    r = await message.reply("`processing...`")
    await delete_all_one()
    await r.edit("Request database 01 Cleared ✅" )
    
@Bot.on_message(filters.command('clear_req_2') & filters.private & filters.user(ADMINS))
async def purge_req_two(bot, message):
    r = await message.reply("`processing...`")
    await delete_all_two()
    await r.edit("Request database 02 Cleared ✅" )
