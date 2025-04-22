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
from learning_platform_app.views import HomePageView, CourseDetailView, AboutPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),  # Updated to use the class-based view
    path('course/<int:course_id>/', CourseDetailView.as_view(), name='course_detail'),  # Updated to use the class-based view
    path('about/', AboutPageView.as_view(), name='about'),  # Updated to use the class-based view
]
