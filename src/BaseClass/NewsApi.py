import requests

from .. import settings


class NewsAPI:

    BaseUrl = "https://newsapi.org/v2"
    headers = {
        'Content-Type': 'application/json'
    }

    def __init__(self, NEWS_API_KEY):
        self.params = {
            'apikey': NEWS_API_KEY,
        }

    @staticmethod
    def cleaned_data(response):
        """
            Extracts Needed data from response
            and returns it as a dictionary.
        """

        clean_data = {
            'headline': response.get('title'),
            'link': response.get('url'),
            'source': 'newsapi'
        }
        return clean_data

    def get_everything(self, query_parameter, pagesize: int = 10):
        """
            Searches every article published over 80,000
            different sources in the past 3 years.
            Ideal for news analysis and article discovery.
        """
        path = NewsAPI.BaseUrl + "/everything"
        params = {
            'q': query_parameter,
            'pageSize': pagesize,
            **self.params
        }
        response = requests.get(path, params=params, headers=NewsAPI.headers)
        if response.status_code != 200:
            return None
        else:
            response = response.json()
            return list(map(NewsAPI.cleaned_data, response.get('articles')))

    def headlines(self):
        """
            Returns breaking news headlines for countries, categories,
            and singular publishers.
            Ideal for news tickers or anywhere you want to
            use live up to date news headlines.
        """
        path = NewsAPI.BaseUrl + "/top-headlines"
        params = {
            'category': 'general',
            **self.params
        }
        response = requests.get(path, params=params, headers=NewsAPI.headers)
        if response.status_code != 200:
            return None
        else:
            response = response.json()
            return list(map(NewsAPI.cleaned_data, response.get('articles')))
