class UserData:
    def __init__(self):
        self.last_error: str = None 

class UserDataManager:
    def __init__(self):
        self.users_data: dict[int, UserData] = {}
    
    def get(self, user_id: int):
        if user_id not in self.users_data:
            ud = UserData()
            self.users_data[user_id] = ud
            return ud
        
        return self.users_data[user_id]

    def reset(self, user_id: int):
        self.users_data[user_id] = UserData()