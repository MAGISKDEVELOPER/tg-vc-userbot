# import logging
from os import environ

from pyrogram import Client, idle

API_ID = int(environ["21124451"])
API_HASH = environ["d0c75e0e8ae1f79ddad10a033411f9ed"]
SESSION_NAME = environ["BQCJbNuNhD5e5rcC1P7h0XKFBOHfvh5Ir-TkEOrULq7ho-ngxaIdzJsuyxLAnzlWy8H41Fmt2jmcVulpDGiMh1sHNbXH3BTE1gE4fBspSk_o79nY4QT6ntdU_fBqg7mImh48vAzYu93-A_p_FPiqssjwB0FUWU8xDRkDtNr1eY1eszzlbBDp-u51zA20okv7OuQ5-rLy9OqTzyu9bTjV7bKYiiNj_QoLWt424XT7_79AwTvdqaPjltB8tHxv919bxam0lfeJnCt8P06SOuZskvtlxRTEF4JvnPANnFx9g16BGQRLkI3TdSwEXY5E4snwJDAbjHgxRDxlRtHh0GqJ4D56AAAAAWTX6CIA"]

PLUGINS = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
