from django.shortcuts import render
from .models import Course
from django.views import View

# Create your views here.
class HomePageView(View):
    def get(self, request):
        courses = Course.objects.all()
        course_name = request.GET.get('search_course')
        if course_name != '' and course_name is not None:
            courses = courses.filter(title__icontains=course_name)
        context = {
            'courses': courses,
        }
        return render(request, 'learning_platform_app/home.html', context)
    

class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        context = {
            'course': course,
        }
        return render(request, 'learning_platform_app/detail.html', context)
    
class AboutPageView(View):
    def get(self, request):
        return render(request, 'learning_platform_app/about.html')
    
class CoursePageView(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {
            'courses': courses,
        }
        return render(request, 'learning_platform_app/courses.html', context)