import asyncio
from fastapi import FastAPI

from src.routers import api_router
from run_task import reddit_data, newsApi_data

app = FastAPI()

app.include_router(api_router.router)


# @app.on_event("startup")
# def startup_event():
#   pass


@app.get("/name")
async def testing():
    query = "fastapi"
    limit = 3
    reddit_result = await reddit_data(query, limit)
    newsapi_result = await newsApi_data(query, limit)

    return {'data': [reddit_result, newsapi_result]}
