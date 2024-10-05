#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 9671629))
API_HASH = getenv("API_HASH", "be5c84e9dc1ca0e2b53d54b71e575124")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7390916656:AAFwogkE9thP-ntxW3vjH-a1RmlhcrwzcmU")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Anubarlo:Anubarlo@cluster0.ioiefbq.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002059513294"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7291869416))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Heroku-Back/Red-Wine_Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

CH_US = getenv("CH_US", "z_zzz8")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/O_P_G")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/QU_QUU")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "True"))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @T66bot on Telegram
STRING1 = getenv("STRING_SESSION", "BAGB5kgAnDP1yncq69ESO_5WebuylQNUJV3oEosm_43J48gfleW0auqJ7nXLkI8tTZQiHBQN9w-cq0BS7j5qxBR7Pwv9mlTmnKzMfNqN7CLfU0f1pKl8a8NB0-KsRbt-hIXGpoAnb7H6lY3xIAxYQv_afC4PJh1n2WK2-tfcWrQmv4tN1w-98co7GVgBD71sAnkUEt-3f0XCC-zOyyhtdy1N0JlSxpyDn7ruDi01yAOgcjLv-z_AyZMpqZkmrO4nvthelpMXnpn0uxqMgzSIbpx35Rc__YwGyvpZ0Z0-ueJvyYVGAefmRcf6crHLox731eifrbxI6UWyqQ_3k_Tzf8BrxAlVowAAAAEvAALVAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/f7e1acf9338cc453a87ad.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
