from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*', ]
INSTALLED_APPS += [
    'haystack',
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
