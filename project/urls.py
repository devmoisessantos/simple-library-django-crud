"""
Configuração de URLs para o projeto Applet.

A lista `urlpatterns` roteia URLs para views. Para mais informações, consulte:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Exemplos:
Views baseadas em funções:
    1. Adicione um import:  from my_app import views
    2. Adicione uma URL à lista:  path('', views.home, name='home')
Views baseadas em classes:
    1. Adicione um import:  from other_app.views import Home
    2. Adicione uma URL à lista:  path('', Home.as_view(), name='home')
Incluindo outra configuração de URLs:
    1. Importe a função include: from django.urls import include, path
    2. Adicione uma URL à lista:  path('blog/', include('blog.urls'))
"""

from project import views  # Importando as views
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URL para o painel de administração do Django
    path('admin/', admin.site.urls),

    # URLs para as views
    path('', include('lib.urls')),  # Página inicial

    # Exemplo de inclusão de URLs de outro aplicativo
    # path('app/', include('app.urls')),

]

# Ativar o Django Debug Toolbar no ambiente de desenvolvimento
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    # Servir arquivos de mídia apenas no modo de desenvolvimento
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# Recomendações:
# 1. Use `include` para organizar as URLs dos aplicativos.
# 2. Certifique-se de que cada app tenha seu próprio arquivo de URLs (exemplo: `app/urls.py`).
