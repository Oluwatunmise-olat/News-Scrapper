from fastapi import FastAPI

from src.routers import api_router
from src.BaseClass.RedditApi import settings, Reddit
from src.BaseClass.NewsApi import settings, NewsAPI

app = FastAPI()

app.include_router(api_router.router)


# @app.on_event("startup")
# def startup_event():
""" Runs the following events before the application starts """
# reddit_instance = Reddit(settings.CLIENT_ID, settings.SECRET_KEY)
# print(reddit_instance.access_token)
# print(reddit_instance.get_latest_news('fastapi', 1))
#  'rediit': reddit_instance.get_latest_news('fastapi', 2)

# newsapi_instance = NewsAPI(settings.NEWS_API_KEY)
# print(newsapi_instance.params)


@app.get("/name")
def testing():
    return {'data': settings.config}
