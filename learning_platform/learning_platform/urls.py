"""
URL configuration for learning_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from learning_platform_app.views import HomePageView, CourseDetailView, AboutPageView, CoursePageView
from user import views
=======
from learning_platform_app.views import HomePageView, CourseDetailView, AboutPageView
from user.views import UserRegistrationView
>>>>>>> 53dee7202975b4351683cf584b71b9914ad1ba55


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),  # Updated to use the class-based view
    path('course/<int:course_id>/', CourseDetailView.as_view(), name='course_detail'),  # Updated to use the class-based view
    path('about/', AboutPageView.as_view(), name='about'),  # Updated to use the class-based view
<<<<<<< HEAD
    path('course/', CoursePageView.as_view(), name='course'),  # Updated to use the class-based view
    path('register/', views.register, name='register'),  # Registration page
=======
    path('register/', UserRegistrationView.as_view(), name='register'),  # Updated to use the class-based view
>>>>>>> 53dee7202975b4351683cf584b71b9914ad1ba55
]
