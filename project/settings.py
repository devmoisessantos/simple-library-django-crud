"""
Configurações do Django para o projeto Applet.

Gerado por 'django-admin startproject' usando o Django 5.1.4.

Para mais informações sobre este arquivo, veja:
https://docs.djangoproject.com/en/stable/topics/settings/

Para a lista completa de configurações e seus valores, consulte:
https://docs.djangoproject.com/en/stable/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as messages

# Configurações de mensagens
MESSAGE_TAGS = {
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger'
}

# Caminhos principais do projeto
BASE_DIR = Path(__file__).resolve().parent.parent


# Configurações rápidas para desenvolvimento - inadequadas para produção
# Consulte https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

# ATENÇÃO: Mantenha a chave secreta em sigilo em produção!
SECRET_KEY = 'django-insecure-slbfl#@sz470r%2&^=7+(gem3cd8b(5e_#bn_o0boam#ckl&5a'

# ATENÇÃO: Não execute com DEBUG ativado em produção!

DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'


# Adicione os domínios permitidos na produção.
ALLOWED_HOSTS = []


# Definição das aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Recomendações para desenvolvimento
    'debug_toolbar',  # Para debug e monitoramento
    'django_extensions',  # Ferramentas adicionais como shell_plus
    'lib'
]

# Middleware (processadores de requisições/respostas)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Middleware para desenvolvimento
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Configuração de URLs
ROOT_URLCONF = 'project.urls'

# Configurações de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Diretório adicional para templates
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

# Aplicação WSGI
WSGI_APPLICATION = 'project.wsgi.application'


# Configuração do banco de dados
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validação de senhas
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},  # Recomendação para aumentar a segurança
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalização
# https://docs.djangoproject.com/en/stable/topics/i18n/
LANGUAGE_CODE = 'pt-br'  # Idioma configurado para português do Brasil

TIME_ZONE = 'America/Sao_Paulo'  # Configuração para o fuso horário do Brasil

USE_I18N = True

USE_TZ = True


# Arquivos estáticos (CSS, JavaScript, Imagens)
# https://docs.djangoproject.com/en/stable/howto/static-files/
STATIC_URL = 'static/'
# Diretório para arquivos estáticos do projeto
STATICFILES_DIRS = [BASE_DIR / 'static']

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# Configurações para arquivos de mídia (uploads de usuários)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Tipo padrão para chaves primárias
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Recomendação para o modo de desenvolvimento
INTERNAL_IPS = ['127.0.0.1']  # Necessário para o Django Debug Toolbar

# Configuração para e-mails (exemplo básico)
# Apenas para desenvolvimento
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
