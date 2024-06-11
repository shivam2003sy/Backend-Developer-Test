from cachetools import TTLCache

# Cache for storing posts with a TTL of 5 minutes
cache = TTLCache(maxsize=100, ttl=300)
