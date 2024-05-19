from django.urls import path
from dashboard_app.views import dashboard_view, logout_view


urlpatterns = [
      path('', dashboard_view, name='dashboard'),
      path('logout', logout_view, name='logout')
  ]


