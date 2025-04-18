from pyrogram import Client, filters
from database.database import *
from bot import Bot
from config import ADMINS




@Bot.on_message(filters.command("setfsub") & filters.user(ADMINS))
async def set_force_sub(client, message):
   
    try:
        args = message.text.split()
        if len(args) != 2 or not args[1].startswith("-100"):
            return await message.reply_text("Please provide exactly one valid channel ID in the format:\n`/setfsub -100XXXXXXXXX`")

        channel_id = args[1]

        # Try to get or generate invite link
        try:
            chat = await client.get_chat(channel_id)
            if not chat.invite_link:
                invite_link = await client.export_chat_invite_link(channel_id)
            else:
                invite_link = chat.invite_link  # unified variable name
        except Exception as e:
            return await message.reply_text(
                f"Error: {e}\n\n"
                f"Make sure:\n"
                "- Bot is added to the channel\n"
                "- Bot is admin\n"
                "- Bot has 'Invite via Link' permission\n"
                f"Channel ID used: {channel_id}"
            )

        # Save to DB (await it!)
        set_force_sub_channel(channel_id, invite_link)
        

        await message.reply_text(
            f"✅ Force subscription channel set successfully!\n\n"
            f"**Channel ID:** `{channel_id}`\n"
            f"**Invite Link:** {invite_link}"
        )

    except Exception as e:
        print(f"Unhandled error: {str(e)}")

@Bot.on_message(filters.command("getfsub") & filters.user(ADMINS))
async def get_force_sub(client, message):
    try:
        # Fetch the current force subscription channel from MongoDB
        channel_id = get_force_sub_channel()
        if channel_id:
            await message.reply_text(f"Current Force Sub Channel ID: {channel_id}")
        else:
            await message.reply_text("No Force Sub Channel has been set.")
    except Exception as e:
        print(f"Error: {str(e)}")  # Log the error silently

@Bot.on_message(filters.command("delfsub") & filters.user(ADMINS))
async def delete_force_sub(client, message):
    global invite_link
    try:
        delete_force_sub_channel()
        await message.reply_text("❌ Force subscription channel has been deleted from the database.")
        invite_link=None
    except Exception as e:
        print(f"Error in /delfsub: {e}")
        await message.reply_text("An error occurred while deleting the force sub channel.")
