"""
Configuração WSGI para o projeto Applet.

Este arquivo expõe a callable WSGI como uma variável de nível de módulo chamada `application`.

Para mais informações sobre este arquivo, consulte:
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Define o módulo de configurações padrão do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Cria a aplicação WSGI para servir as requisições
application = get_wsgi_application()

# Recomendações para produção:
# 1. Configure o servidor web (como Gunicorn ou uWSGI) para usar esta aplicação WSGI.
# 2. Certifique-se de que as configurações de produção estejam corretamente definidas
#    no arquivo settings.py (DEBUG=False, ALLOWED_HOSTS configurado, entre outros).
