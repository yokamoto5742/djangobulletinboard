import os
import environ
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


env = environ.Env()
env.read_env('.env')


# settings.pyからそのままコピー
SECRET_KEY = 'django-insecure-ie3aw0wi729sbkn%++q*(jwl_fzu+_duf6+ax00-(n_y@fhm0y'

BASE_DIR = Path(__file__).resolve().parent.parent

# settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': env.get_value('DATABASE_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env.get_value('DATABASE_DB', default=os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': env.get_value('DATABASE_USER', default='django_user'),
        'PASSWORD': env.get_value('DATABASE_PASSWORD', default='password'),
        'HOST': env.get_value('DATABASE_HOST', default='localhost'),
        'PORT': env.get_value('DATABASE_PORT', default='5432'),
    }
}

DEBUG = True  # ローカルでDebugできるようになります。
