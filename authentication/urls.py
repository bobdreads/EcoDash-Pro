from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.register_user, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
]
