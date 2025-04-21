import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7427035170:AAHZkmKjv97Ls742O2vr28TjC5LWltbGFwg")
API_ID = int(os.environ.get("API_ID", "25797857"))
API_HASH = os.environ.get("API_HASH", "77717127ece56fac64ebea6250db8bb7")


OWNER_ID = int(os.environ.get("OWNER_ID", "6693549185"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Venkat3823:Venkat3823@cluster0.ig0oc9y.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "Naruto_TAF")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002093054178"))

FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002448901304"))

REQUEST_CHANNEL_1 = int(os.environ.get("REQUEST_CHANNEL_1", "-1002460804912"))

FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002635387240"))

REQUEST_CHANNEL_2 = int(os.environ.get("REQUEST_CHANNEL_2", "0"))



START_PIC = os.environ.get("START_PIC", "https://4kwallpapers.com/images/wallpapers/naruto-uzumaki-3840x2160-18710.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://files.catbox.moe/3gaa9p.jpg")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1200")) # auto delete in seconds


PORT = os.environ.get("PORT", "8020")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[7043973899]
    for x in (os.environ.get("ADMINS", "7043973899").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hᴇʟʟᴏ {mention}\n\n<b>I Aᴍ Aɴɪᴍᴇ Bᴏᴛ I Wɪʟʟ Gɪᴠᴇ Yᴏᴜ Aɴɪᴍᴇ Fɪʟᴇs Fʀᴏᴍ <a href=https://t.me/Anime_Tamil_Hub>Aɴɪᴍᴇ Tᴀᴍɪʟ Hᴜʙ</a></b>.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {mention}\n\n<b>Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟs Tᴏ Gᴇᴛ Aɴɪᴍᴇ Fɪʟᴇs\n\nKɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Cʜᴀɴɴᴇʟs\n\nIғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ɢᴇᴛ ғɪʟᴇ ᴄʜᴇᴄᴋ <a href=https://t.me/Anime_Tamil_Hub/4>Tᴜᴛᴏʀɪᴀʟ</a></b>")




ADMINS.append(OWNER_ID)
ADMINS.append(6693549185)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

class Txt(object):
    about = f"""<b>╭───────────⍟
├➽ Dᴇᴠᴇʟᴏᴩᴇʀ : <a href='tg://user?id={6693549185}'>Mᴏᴏɴ</a>
├➽ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pʏʀᴏɢʀᴀᴍ</a>
├➽ Lᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>Pʏᴛʜᴏɴ 3</a>
├➽ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : <a href=https://t.me/Anime_Tamil_Hub>Aɴɪᴍᴇ Tᴀᴍɪʟ Hᴜʙ</a>
├➽ Mᴀɪɴ Cʜᴀɴɴᴇʟ : <a href=https://t.me/Anime_Tamil_Hub>Aɴɪᴍᴇ Tᴀᴍɪʟ Hᴜʙ</a>
├➽ Mᴀɪɴ Gʀᴏᴜᴘ : <a https://t.me/+8bE6LN_37EBmNGNl>𝘼𝙣𝙞𝙢𝙚 𝙂𝙖𝙣𝙜 𝙏𝙖𝙢𝙞𝙡</a></b>
╰───────────────⍟ """
