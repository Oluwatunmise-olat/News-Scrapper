from fastapi import FastAPI

from routers import news_api_router

app = FastAPI()

app.include_router(news_api_router.router)
