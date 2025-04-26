from django.urls import path
from learning_platform_app.views import HomePageView, CourseDetailView, AboutPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Updated to use the class-based view
    path('course/<int:course_id>/', CourseDetailView.as_view(), name='course_detail'),  # Updated to use the class-based view
    path('about/', AboutPageView.as_view(), name='about'),  # Updated to use the class-based view
]
