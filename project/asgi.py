"""
Configuração ASGI para o projeto Applet.

Este arquivo configura a aplicação ASGI, tornando-a pronta para o uso em produção.
A callable ASGI é exposta como uma variável de nível de módulo chamada `app`.

Para mais detalhes, visite:
https://docs.djangoproject.com/en/stable/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Define o módulo de configurações padrão do Django para o comando 'asgi'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Cria a aplicação ASGI para processar requisições HTTP assíncronas.
app = get_asgi_application()

# Configurações adicionais para funcionalidades assíncronas, como WebSockets, podem ser adicionadas aqui.
