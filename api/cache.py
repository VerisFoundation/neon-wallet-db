from flask.ext.cache import Cache
from werkzeug.contrib.cache import MemcachedCache
from .server import application
import os

# Constants
USE_MEMCACHE = True

## Cache
cache_config = {}
cache_config['CACHE_TYPE'] = 'simple'

### Memcache

if USE_MEMCACHE:
    cache_config['CACHE_TYPE'] = 'flask_cache_backends.bmemcached'
    cache_config['CACHE_MEMCACHED_USERNAME'] = None
    cache_config['CACHE_MEMCACHED_PASSWORD'] = None
    cache_config['CACHE_MEMCACHED_SERVERS'] = os.environ.get('MEMCACHED_URL')

cache = Cache(application, config=cache_config)
