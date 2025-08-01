class DataBase:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name):
        if user_id in self.users:
            raise ValueError("User alredy added.") 

        self.users[user_id] = name
        return True

    def get_user(self, user_id):
        return self.users.get(user_id, None)

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]               