# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "Cinemaa_Boxoffice Link Generator"
bisal_channel = "https://telegram.me/Cinemaa_Boxoffice"
bisal_grp = "https://t.me/+dby5msMqTOBjMGU1"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '20650942'))
    API_HASH = str(getenv('API_HASH', '9744c99858433c55c279cce6827d36a4'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6702817700:AAGuIyq8DTILFJSJ91HVa56iSdgHTkt-oRI'))
    name = str(getenv('name', 'FiletolinkCBbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002114057590'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002114057590'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1947565279").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Rishisin07'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://darkbing155:password1234@cluster0.rvky2.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'moviesworld738')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001844691460")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "-1001844691460")).split()))   
    
