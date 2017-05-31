from cachetools import TTLCache

cache = TTLCache(maxsize=50,ttl=300)