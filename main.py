from fastapi import FastAPI

from src.routers import api_router

app = FastAPI()

app.include_router(api_router.router)


# @app.on_event("startup")
# def startup_event():
#   pass
