import asyncio
from fastapi import APIRouter, status, HTTPException
from typing import Optional

from . import schemas
from ..run_task import reddit_data, newsApi_data

router = APIRouter(
    prefix='/news',
    tags=['News Aggregator']
)


@router.get('/', status_code=status.HTTP_200_OK)
async def NewsEndpoint(query: Optional[str] = None, limit: int = 1):

    reddit_result = await reddit_data(query, limit)
    newsapi_result = await newsApi_data(query, limit)

    return {'data': [reddit_result, newsapi_result]}
