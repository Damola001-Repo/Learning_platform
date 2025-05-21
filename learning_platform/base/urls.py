from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('courses/', views.coursesPage, name='courses'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('course-details/<str:pk>', views.courseDetails, name='course-details'),
    path('payment/', views.payment, name='payment'),
    path('profile/', views.profile, name='profile'),
]