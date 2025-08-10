import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "20415731")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "8282154810:AAF0fz0OhHxpZeFlVCVhfs2PYl9-PAKz_ms") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7789056658:AAGpgwF3U5Hq7vYUDFuHEEc4M4QZqcQo484") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'None') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://meow:meow@meow.a6bo1.mongodb.net/?retryWrites=true&w=majority&appName=meow")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","moe") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "6440021089")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002134572304')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/897ca838f36cdd3861763-347257045a8f7806f0.jpg")




    
    
    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
