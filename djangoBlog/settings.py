"""
Django settings for djangoBlog project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import sys
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#^z=ncuc)8az8$d*k2#m-k7ae^pqp=3o_f1_*a$s8a)leevz@e'

# SECURITY WARNING: don't run with debug turned on in production!
# 通过判断主机ip来实现是否开启debug模式
if socket.gethostbyname(socket.gethostname())[:3] == '192':
    DEBUG = True
    ALLOWED_HOSTS = ['127.0.0.1', '192.168.2.113']
else:
    DEBUG = False
    ALLOWED_HOSTS = ['www.zhangwurui.com', 'zhangwurui.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites'
]

# 个人应用
PERSONAL_APPS = [
    'apps.blog.apps.BlogConfig',
    'apps.comments.apps.CommentConfig',
    'apps.accounts.apps.AccountsConfig',
]

# 添加站点,用于生产xml站点地图

# 第三方应用
EXTRA_APPS = [
    'mdeditor',
]

INSTALLED_APPS += PERSONAL_APPS + EXTRA_APPS

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.blog.custom_processors.global_variable',
            ],
            'builtins': [
                'django.templatetags.static',
            ]
        },
    },
]

WSGI_APPLICATION = 'djangoBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web',
        'USER': 'root',
        'PASSWORD': '950312',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

# 用户模型
AUTH_USER_MODEL = 'accounts.OAuth'

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True
# 国际化,支持多种语言

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# 设置静态文件路径
STATIC_URL = '/static/'
# 部署网站时搜集静态文件
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 地理位置数据库
GEOIP_PATH = os.path.join(BASE_DIR, 'static/real_address/GeoLite2-City.mmdb')

# 搜集静态文件时要注释 STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
)

# 设置文件上传路径
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

# 邮件信息配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
# 是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
EMAIL_HOST = 'smtp.163.com'
# 发送邮件的邮箱 的 SMTP 服务器，这里用了163邮箱
EMAIL_PORT = 25
# 发件箱的SMTP服务器端口
EMAIL_HOST_USER = '15871930413@163.com'
# 发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'zrui950312'
# 发送邮件的邮箱密码(这里使用的是授权码)


# 增加自定义后套验证路径
AUTHENTICATION_BACKENDS = (
    'accounts.backends.CustomBackend',
)
