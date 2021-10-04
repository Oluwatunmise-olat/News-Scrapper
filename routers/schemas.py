from pydantic import BaseModel


class ListSchema(BaseModel):
    headline: str
    link: str
    source: str

    class Config():
        orm_mode = True


class SearchSchema(BaseModel):
    query: str
