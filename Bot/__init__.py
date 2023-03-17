import os, sys, logging
from pyrogram import Client 

if os.path.exists('error.log'):
    os.remove('error.log')
        
#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO, filename='error.log')
LOG = logging.getLogger("Bot by @soheru")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '5442493323:AAHPw8TNe0hh2zCAQKm_2O2o6KdmQ3Okgf8') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 6534707)) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', '4bcc61d959a9f403b2f20149cbbe627a')# Telgram App hash  
OWNER_ID = int(os.environ.get('OWNER_ID', 953362604))
MONGO_DB = os.environ.get("MONGO_DB", 'mongodb+srv://Uploader:Uploader@cluster0.ba0ppxa.mongodb.net/?retryWrites=true&w=majority') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", -1001843564893)
BOT_NAME = os.environ.get('BOT_NAME', 'Hptecbot')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @soheru || Telegram @sohailkhan_indianime ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
