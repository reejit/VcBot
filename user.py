from config import Config
from pyrogram import Client

USER = Client(
    session_name=Config.HELL_SESSION,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,  
    
)
USER.run()
