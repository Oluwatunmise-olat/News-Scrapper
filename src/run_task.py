import asyncio
from typing import Optional

from src.BaseClass.RedditApi import settings, Reddit
from src.BaseClass.NewsApi import settings, NewsAPI


async def reddit_data(query: Optional[str] = None, limit: Optional[int] = None):
    # Instantiate class Instances
    reddit_instance = Reddit(settings.CLIENT_ID, settings.SECRET_KEY)
    if not limit:
        requested_data = reddit_instance.get_latest_news(query)
    requested_data = reddit_instance.get_latest_news(query, limit=limit)
    return requested_data


async def newsApi_data(query: Optional[str] = None, limit: Optional[int] = None):
    # Instantiate class Instances
    newsapi_instance = NewsAPI(settings.NEWS_API_KEY)
    if not limit:
        requested_data = newsapi_instance.get_everything(query)
    requested_data = newsapi_instance.get_everything(query, pagesize=limit)
    return requested_data

"""
async def main(query, limit: Optional[int] = None):
    reddit = loop.create_task(reddit_data(query=query, limit=limit))
    newsapi = loop.create_task(newsApi_data(query=query, limit=limit))
    await asyncio.wait([reddit, newsapi])
    return reddit_result, newsapi_result


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    reddit_result, newsapi_result = loop.run_until_complete(main('asyncio', 2))
"""
