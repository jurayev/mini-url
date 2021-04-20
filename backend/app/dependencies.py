from functools import lru_cache
from fastapi import Depends
from redis import Redis

from .config import settings
from .core.shortener import Shortener


@lru_cache()
def get_db() -> Redis:
    # db = Redis(host=settings.REDIS_HOST,
    #            port=settings.REDIS_PORT,
    #            password=settings.REDIS_PASSWORD,
    #            decode_responses=True)
    db = Redis.from_url(url=settings.REDIS_URL, decode_responses=True)
    return db


@lru_cache()
def get_shortener(db: Redis = Depends(get_db)) -> Shortener:
    return Shortener(db)
