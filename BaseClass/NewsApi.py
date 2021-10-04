import requests

from .settings import News_API_KEY


class NewsAPI:

    BaseUrl = "https://newsapi.org/v2"
    params = {
        'apikey': News_API_KEY,
    }
    headers = {
        'Content-Type': 'application/json'
    }

    @staticmethod
    def cleaned_data(response):
        clean_data = {
            'headline': response.get('title'),
            'link': response.get('url'),
            'source': 'newsapi'
        }
        return clean_data

    @staticmethod
    def get_everything(query_parameter):
        """
            Searches every article published over 80,000
            different sources in the past 3 years.
            Ideal for news analysis and article discovery.
        """
        path = NewsAPI.BaseUrl + "/everything"
        params = {
            'q': query_parameter,
            ***NewsAPI.params
        }
        response = requests.get(path, params=params, headers=NewsAPI.headers).json()
        if response.status_code != 200:
            return None
        else:
            return list(map(NewsAPI.cleaned_data, response.get('articles')))

    @staticmethod
    def headlines():
        """
            Returns breaking news headlines for countries, categories,
            and singular publishers.
            Ideal for news tickers or anywhere you want to
            use live up to date news headlines.
        """
        path = NewsAPI.BaseUrl + "/top-headlines"
        params = {
            'category': 'general',
            ***NewsAPI.params
        }
        response = requests.get(path, params=params, headers=NewsAPI.headers).json()
        if response.status_code != 200:
            return None
        else:
            return list(map(NewsAPI.cleaned_data, response.get('articles')))


->headline, link, source
