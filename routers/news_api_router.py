from fastapi import APIRouter, status, HTTPException
# import asyncio

from . import schemas

router = APIRouter(
    prefix='/news',
    tags=['newsapi']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=schemas.ListSchema)
def list():
    return {'headline': 'from newsapi', 'link': 'www.from reddit api', 'source': 'Newsapi'}


@router.get('/search/', status_code=status.HTTP_200_OK)
def search(query: schemas.SearchSchema):
    return {'data': "ff"}
