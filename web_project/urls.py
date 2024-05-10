"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", include("dashboard_app.urls")),
    path("accounts/profile/", include("dashboard_app.urls")),
    path("cadastros/", include("cadastro_app.urls")),
    path("audita/", include("audit_app.urls")),
    path("solicitacao/", include("sol_app.urls")),
    path("eventos/", include("evento_app.urls")),
    path("usuarios/", include("usuario_app.urls")),
    path("historico/", include("consulta_app.urls")),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path("usuarios/cadastro_usuario/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),


    path("admin/", admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
