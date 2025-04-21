from django.shortcuts import render
from .models import Course, HomePage
from django.views import View

# Create your views here.
class HomePageView(View):
    def get(self, request):
        # Logic to fetch data from the database and render the home page
        # For example, you might want to fetch all courses and pass them to the template
        homepage_data = HomePage.objects.first()  # Assuming you have only one HomePage object
        courses = Course.objects.all()
        context = {
            'homepage_data': homepage_data,
            'courses': courses,
        }
        return render(request, 'learning_platform_app/home.html', context)