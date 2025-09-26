from telegram import Update, User
from src.init.app import botm

async def start(update: Update, _):
    chat = update.effective_chat
    if chat and chat.type != "private":
        print(f"{chat.id} написал /start не в личном чате")
        return
    
    if update.message:
        user = update.message.from_user
    elif update.callback_query:
        user = update.callback_query.from_user
    else:
        print("Пользователь написал, но не было ни message, ни callback_query")
        return
    assert isinstance(user, User)
    
    user_id = user.id
    await start_inner(user_id)

async def start_inner(user_id: int):  
    if botm.config.development_mode and         user_id not in botm.config.admin_list:
        print(f"{user_id} написал /start и не был допущен [development mode]")
        return
    
    print(f"{user_id} написал /start")
    
    sud = botm.system_user_data.get(user_id)
    if sud and sud.screen:
        try: await sud.screen.delete(botm.bot)
        except: ...
    
    botm.system_user_data.reset(user_id)
    botm.reset_user_data(user_id)
    
    await botm.screen.set_by_name(user_id, "welcome")