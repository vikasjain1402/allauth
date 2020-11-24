import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_MY_PROJECT']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', 
    #  'social_app.apps.SocialAppConfig',  
    'social_app',
     
 
    'allauth',   
    'allauth.account',   
 'allauth.socialaccount',   
    'allauth.socialaccount.providers.google'  
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_project.wsgi.application'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 500 * 60 
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = False

AUTHENTICATION_BACKENDS = (
 'django.contrib.auth.backends.ModelBackend',
 'allauth.account.auth_backends.AuthenticationBackend',
 )


SITE_ID = 3
LOGIN_REDIRECT_URL = '/'

ACCOUNT_EMAIL_VERIFICATION=True


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'APP':{
            'client_id':os.environ['GOOGLE_API_CLIENT_KEY_COR'],
            'secret':os.environ['GOOGLE_API_SECRET_KEY_COR'],
            'key':''
        }
        #,
        #'AUTH_PARAMS': {
        #    'access_type': 'online',
        #}
    }
}
ACCOUNT_AUTHENTICATION_METHOD='email'
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_VERIFICATION='mandatory'
ACCOUNT_USERNAME_REQUIRED=False



#AUTH_USER_MODEL='accounts.user'
#For sendding mails
import os

EMAIL_HOST_USER=os.environ['GMAIL_USERNAME']
EMAIL_HOST_PASSWORD=os.environ["GMAIL_PASSWORD"]
DEFAULT_FROM_EMAIL=EMAIL_HOST_USER
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'

#for user authentification

#EMAIL_ACTIVE_FIELD = 'is_active'
EMAIL_SERVER = 'smtp.gmail.com'
EMAIL_PORT = 587

'''
EMAIL_ADDRESS =os.environ["GMAIL_USERNAME"]
EMAIL_FROM_ADDRESS=os.environ["GMAIL_USERNAME"]

EMAIL_PASSWORD=os.environ["GMAIL_PASSWORD"]

EMAIL_MAIL_SUBJECT="Confirm Your Email"
EMAIL_MAIL_HTML="mail_body.html"
EMAIL_MAIL_PLAIN='mail_body.txt'

EMAIL_PAGE_TEMPLATE = 'confirm_template.html'
EMAIL_PAGE_DOMAIN = 'http://localhost:8000/'

'''



GOOGLE_API_CLIENT_KEY_COR="399894155479-hc6qct1i4lr5col7lidj6hr6pmoojjfp.apps.googleusercontent.com"
GOOGLE_API_SECRET_KEY_COR="d53J0thqnRKUTZwceCybCiU6"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
