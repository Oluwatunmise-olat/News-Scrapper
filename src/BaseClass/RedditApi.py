import requests

from .. import settings


class Reddit:

    BASE_URL = "https://oauth.reddit.com/r"
    HEADERS = {
        'User-Agent': 'ChangeMe/0.1 by olat'
    }

    def __init__(self, client_id, secret_key):
        self.client_id = client_id
        self.secret_key = secret_key
        self.access_token = self.get_access_token()

    def get_access_token(self):
        """
            Gets access_token from reddit to
            make request to endpoints.
        """
        path = "https://www.reddit.com/api/v1/access_token"

        auth = requests.auth.HTTPBasicAuth(self.client_id, self.secret_key)
        data = {
            'grant_type': 'password',
            'username': 'reddit_aggregator',
            'password': 'news_bot13'
        }

        response = requests.post(path, data=data, auth=auth, headers=self.HEADERS)
        token = response.json()
        print(response)
        return token["access_token"]

    @staticmethod
    def cleaned_data(response):
        """
            Extracts Needed data from response
            and returns it as a dictionary.
        """
        clean_data = {
            'headline': response['data']['children']['data']['title'],
            'link': response['data']['children']['data']['url'],
            'source': 'fastapi'
        }
        return clean_data

    def get_latest_news(self, query, limit: int = 10):
        path = self.BASE_URL + f"/{query}/new"
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            **self.HEADERS,
        }
        response = requests.get(path, headers=headers, params={'limit': limit})
        response = response.json()
        print(response)
        return list(map(Reddit.cleaned_data, response))
