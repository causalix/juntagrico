"""
Django settings for solawisi project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8cd-j&jo=-#ecd1jjulp_s*7y$n4tad(0d_g)l=6@n^r8fg3rn'

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'True')=='True'

ALLOWED_HOSTS = ['my.solawisi.ch','solawisi.juntagrico.science', 'localhost',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'juntagrico',
    'impersonate',
    'crispy_forms',
    'solawisi',
]

ROOT_URLCONF = 'solawisi.urls'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','solawisi.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'), #''junatagrico', # The following settings are not used with sqlite3:
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'), #''junatagrico',
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'), #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False), #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
            'debug' : True
        },
    },
]

WSGI_APPLICATION = 'solawisi.wsgi.application'


LANGUAGE_CODE = 'de'

SITE_ID = 2

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS =['%d.%m.%Y',]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware'
]

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

WHITELIST_EMAILS = []

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)
            


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

LOGIN_REDIRECT_URL = "/my/home"

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = 'media'

"""
     Crispy Settings
"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'

"""
     juntagrico Settings
"""
ORGANISATION_NAME = "Solawisi"
ORGANISATION_LONG_NAME = "Solawisi"
ORGANISATION_ADDRESS = {"name":"Solawisi", 
            "street" : "Mühlestrasse",
            "number" : "21",
            "zip" : "8542",
            "city" : "Wiesendangen",
            "extra" : "c/o Monika Steiner"}
ORGANISATION_BANK_CONNECTION = {"PC" : "-",
            "IBAN" : "CH95 0839 0037 1022 1000 0",
            "BIC" : "-",
            "NAME" : "Alternative Bank",
            "ESR" : ""}
INFO_EMAIL = "kontakt@solawisi.ch"
SERVER_URL = "www.solawisi.ch"
ADMINPORTAL_NAME = "my.solawisi.ch"
ADMINPORTAL_SERVER_URL = "https://my.solawisi.ch"
SHARE_PRICE = "250"
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
TIME_ZONE = 'Europe/Zurich'
BUSINESS_YEAR_START = {"day": 1, "month": 6}
MEMBERSHIP_END_MONTH = 5
BUSINESS_YEAR_CANCELATION_MONTH = 3
BYLAWS = "https://wixlabs-file-sharing.appspot.com/api/files/view?instance=B9bsucnOQbjKj-2btEfICAHNNytDuJDtzlGYKTC13hg.eyJpbnN0YW5jZUlkIjoiNTI4MjZkZmQtMWRiNi00MjA1LWFmNWQtYmUwMmFmZDRjNThiIiwiYXBwRGVmSWQiOiIxNTM3YjI0ZS0yOWQxLTZkOGYtYjhlMS1kNjg2MGYyZjcwYjkiLCJtZXRhU2l0ZUlkIjoiMWRhMDY0NGUtNTY5OS00N2I0LTgwM2MtZGE5MzU5N2ZlOGFmIiwic2lnbkRhdGUiOiIyMDIwLTA2LTA4VDE1OjExOjQwLjUzMVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6ImI3Nzc1Y2Y5LTRmOGEtNGZjOC1iZWQ0LWYxOGI0Zjk1NDVhOCIsImJpVG9rZW4iOiI0ZjIyMDliMy00YjJmLTA1YjEtMmY2MS02NDkxZjZhYjJkMjQiLCJzaXRlT3duZXJJZCI6Ijg5ZDJhNjRhLTRmMWMtNGY1My1hNTNiLWE4ZDVhZDA1NjQ2NCJ9&compId=TPASection_kb6hz8ac&libraryItemId=6ceef35f-a0b3-4be7-b0c4-7afb377fc527&errURL=https%3A%2F%2Fwww.solawisi.ch%2Ffile-share%2F"
BUSINESS_REGULATIONS = "https://wixlabs-file-sharing.appspot.com/api/files/view?instance=B9bsucnOQbjKj-2btEfICAHNNytDuJDtzlGYKTC13hg.eyJpbnN0YW5jZUlkIjoiNTI4MjZkZmQtMWRiNi00MjA1LWFmNWQtYmUwMmFmZDRjNThiIiwiYXBwRGVmSWQiOiIxNTM3YjI0ZS0yOWQxLTZkOGYtYjhlMS1kNjg2MGYyZjcwYjkiLCJtZXRhU2l0ZUlkIjoiMWRhMDY0NGUtNTY5OS00N2I0LTgwM2MtZGE5MzU5N2ZlOGFmIiwic2lnbkRhdGUiOiIyMDIwLTA2LTA4VDE1OjExOjQwLjUzMVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6ImI3Nzc1Y2Y5LTRmOGEtNGZjOC1iZWQ0LWYxOGI0Zjk1NDVhOCIsImJpVG9rZW4iOiI0ZjIyMDliMy00YjJmLTA1YjEtMmY2MS02NDkxZjZhYjJkMjQiLCJzaXRlT3duZXJJZCI6Ijg5ZDJhNjRhLTRmMWMtNGY1My1hNTNiLWE4ZDVhZDA1NjQ2NCJ9&compId=TPASection_kb6hz8ac&libraryItemId=1c4185c7-f48b-4af6-bfc5-592a6884fadc&errURL=https%3A%2F%2Fwww.solawisi.ch%2Ffile-share%2F"
