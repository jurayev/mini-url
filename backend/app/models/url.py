from pydantic import BaseModel, HttpUrl


class UrlBase(BaseModel):
    url: HttpUrl


class UrlIN(UrlBase):
    pass
    pass


class UrlOut(UrlBase):

    short_url: HttpUrl
