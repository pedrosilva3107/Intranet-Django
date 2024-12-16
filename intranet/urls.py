"""
URL configuration for intranet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# intranet/urls.py
# intranet/urls.py
from django.contrib import admin
from django.urls import path, include
from usuarios import views as usuarios_views
from home import views as home_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # URLs do app 'usuarios'
    path('login/', usuarios_views.login_view, name="login"),
    path('sair/', usuarios_views.sair, name="sair"),
    path('home/', home_views.home, name='home'),
    path('reiniciar-servidor/', home_views.reiniciar_servidor, name='reiniciar_servidor'),
    
    # Incluir as URLs do app 'pops'
    path('pops/', include('pops.urls')),  # Isso inclui as URLs definidas no 'pops/urls.py'
]


