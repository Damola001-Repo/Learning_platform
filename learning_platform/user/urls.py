from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.userRegistration, name='user-registration'),
    path('login/', views.userLogin, name='user-login'),
    path('logout/', views.userLogout, name='user-logout')
]