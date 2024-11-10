import os

API_ID = API_ID = 16214694

API_HASH = os.environ.get("API_HASH", "7545825d90eb7adae543d59909c73121")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5543709855 ))

LOG = -1001664442987

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5543709855").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


