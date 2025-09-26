from typing import Callable
from telegram.ext import Application
from tg_bot_screen.ptb import BotManager as BaseBotManager
from .user_data import UserDataManager
from .config_manager import ConfigManager

class BotManager(BaseBotManager):
    def __init__(self, application: Application):
        super().__init__(application)
        self.user_data_m = UserDataManager()
        self.config = ConfigManager()
        self.config.load()
        
        self.start_inner: Callable = None
    
    def get_user_data(self, user_id: int):
        return self.user_data_m.get(user_id)

    def reset_user_data(self, user_id: int):
        self.user_data_m.reset(user_id)
        
    async def mapping_key_error(self, user_id: int):
        await self.start_inner(user_id)