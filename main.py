from fastapi import FastAPI

from src.routers import api_router

from src.BaseClass.RedditApi import settings, Reddit

app = FastAPI()

app.include_router(api_router.router)


# @app.on_event("startup")
# def startup_event():
""" Runs the following events before the application starts """
reddit_instance = Reddit(settings.CLIENT_ID, settings.SECRET_KEY)
print(reddit_instance.access_token)
# print(reddit_instance.get_latest_news('fastapi', 1))


@app.get("/name")
def testing():
    return {'data': settings.config, 'access_token': reddit_instance.access_token, 'rediit': reddit_instance.get_latest_news('fastapi', 2)}
