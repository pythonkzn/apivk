import requests
from urllib.parse import urlencode

OAUTH_URL = 'https://oauth.vk.com/authorize'
USER_URL = 'https://vk.com/id'
APP_ID = 6889971

auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status, friends, users',
    'response_type': 'token',
    'v': 5.92
}

TOKEN = '13ae2d8a86eab035fa2519e73305fbe4168b1fd0c48d487dc8dde880253a4470e0f8260cf40ad27aa8f70'

print ('?'.join((OAUTH_URL, urlencode(auth_data))))

class User:
    def __init__(self, id):
        self.id = id

    def get_params(self):
        return {
            'user_id': self.id,
            'user_ids': self.id,
            'access_token': TOKEN,
            'v': 5.92
        }

    def get_friends(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        return response.json()

    def get_users(self):
        params = self.get_params()
        response = requests.get (
            'https://api.vk.com/method/users.get',
            params
        )
        return response.json()

    def __str__(self):
        return (USER_URL + str(self.get_users()['response'][0]['id']))

    def __and__(self, other):
        return list(set(self.get_friends()['response']['items'])& set(other.get_friends()['response']['items']))



user1 = User(169032181)
user2 = User(2925816)

print ((user1 & user2))
print(user1)