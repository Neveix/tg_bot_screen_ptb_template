from .common import *

@botm.dynamic_screen()
async def welcome(user_id: int, **kwargs):
    return [SimpleMessage("Меню", 
        ButtonRows(
             ButtonRow(Button("Пусто", Dummy()))
        ))]
