import requests

class ApiClient:

    def get_user_data(self, user_id):
        res = requests.get(f"https://api.example.com/users/{user_id}")

        if res.status_code == 200:
            return res.json()
        else:
            raise ValueError("User not found") 


class UserService:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_username(self, user_id):
        user_data = self.api_client.get_user_data(user_id)

        return user_data['name'].upper()  