from Mikey.sample_config import Config

class Development(Config):
    API_ID = 1995654  # integer value, dont use ""
    API_HASH = "91aa713a74d1bccb50cd1c03758316bf"
    TOKEN = "1903350099:AAEN0UWc83XdvdiJuypUX4yTUS8_QNX65Pc"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 860540443  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "crazyguy456"
    SUPPORT_CHAT = 'Mikey_Support'  #Your own group for support, do not add the @
    JOIN_LOGGER = -1001457313720  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -1001457313720  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    SQLALCHEMY_DATABASE_URI = 'postgres://syehdvjn:uRPDHjAXJDmMbE2eT52GWPhO_1wA-22j@queenie.db.elephantsql.com/syehdvjn'  # needed for any database modules
    REDIS_URL = 'redis://Sano:Mikey@1234@redis-11643.c245.us-east-1-3.ec2.cloud.redislabs.com:11643/Sano-Manjiro'
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None 
    MONGO_DB_URI = 'mongodb+srv://userge:mikey1234@cluster0.1kyew.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    TEMP_DOWNLOAD_DIRECTORY = "./"
    SPAMWATCH_API = "RhYz0eTllA8s8Bt_tqMqPuTtsE8A9QNJ9ljZ4yEmUjicyWBMoleMAPcFT1ostMkW"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    TEST_STICKER = '' # Test Sticker
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'TQ8WKVECHE0PGZAL'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'ET7SWXXMDBDF'  # Get your API key from https://timezonedb.com/api
    API_OPENWEATHER = 'e0b024078ac33ac535eb0c1ff97368d6'
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    ARQ_API_KEY = 'LRLZAM-NLHKDS-TDLCLI-ZHFIMB-ARQ'
    ARQ_API_URL = 'thearq.tech'
    AI_API_KEY = '4cdebf3f0c71bd620aa2d0041a63737a185dcb2e4c4b7d7ec42d3bf6e035dd04a69f5a064ce0328b2102c5afecbe1c2b9de26460741455376479cbb1fead2e40'  #For chatbot, get one from https://co$
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
