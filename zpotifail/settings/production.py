from .base import *

import dj_database_url


DEBUG=False

ALLOWED_HOST=["*"]

DATABASES = dict()

# lee la variable de entorno de heroku timeout=500s
DATABASES["default"]=dj_database_url.config(conn_max_age=500)

# Donde se van a leer los statics
STATIC_ROOT=os.path.join(os.getcwd(),"static")