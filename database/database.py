import pymongo, os, pyrogram 
from config import DB_URL, DB_NAME, ADMINS, REQUEST_CHANNEL_1
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.enums import ChatMemberStatus
import re
import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait


dbclient = pymongo.MongoClient(DB_URL)
database = dbclient[DB_NAME]
user_data = database['users']#New collection for force subscription


req_one = database['req_one']  
req_two = database['req_two']




async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

async def is_requested_one(filter, client, update):
    # Check if the user ID exists in the `req_one` collection
    user = await get_req_one(update.from_user.id)
    if user:
        return True
    try:
        member = await client.get_chat_member(chat_id = REQUEST_CHANNEL_1, user_id = update.from_user.id)
    except UserNotParticipant:
        return False

    if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]:
        return False
    else:
        return True 
        
    
async def is_requested_two(message):
    user = await get_req_two(message.from_user.id)
    if user:
        return True
    if message.from_user.id in ADMINS:
        return True
    return False

async def add_req_one(user_id):
    try:
        if not await get_req_one(user_id):
            await req_one.insert_one({"user_id": int(user_id)})
            return
    except:
        pass
        
async def add_req_two(user_id):
    try:
        if not await get_req_two(user_id):
            await req_two.insert_one({"user_id": int(user_id)})
            return
    except:
        pass


async def get_req_one(user_id):
    return req_one.find_one({"user_id": int(user_id)})

async def get_req_two(user_id):
    return req_two.find_one({"user_id": int(user_id)})

async def delete_all_one():
    req_one.delete_many({})

async def delete_all_two():
    req_two.delete_many({})





subscribed3 = filters.create(is_requested_one)





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
