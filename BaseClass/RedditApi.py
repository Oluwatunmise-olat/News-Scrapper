import requests


class Reddit:
    def __init__(self, client_id, secret_key):
        self.client_id = client_id
        self.secret_key = secret_key
        self.access_token = ''

    def get_access_token(self):
        pass
