from .common import *


# SECRET_KEY = 'development-secret-key'
SECRET_KEY = '=hm@ily9+g#1@0f&u#9(gpb216l#09)05f9h22y(d7*h9#i5--'

DEBUG = True
ALLOWED_HOSTS = ['*','101.133.210.166']
HAYSTACK_CONNECTIONS['default']['URL'] = 'http://172.18.0.2:9200/'
