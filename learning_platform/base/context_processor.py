# yourapp/context_processors.py
from .models import Student, Instructor    


def user_profile_image(request):
    if request.user.is_authenticated:
        user = request.user
    try:
        if user.role == 'student':
            user_email = user.student
            user = Student.objects.get(user__email=user_email)
            context = {
                'avatar': user.avatar.url
            }
        elif user.role == 'instructor':
            user_email == user.instructor
            user = Instructor.objects.get(user__email=user_email)
            context = {
                'avatar': user.avatar.url
            }
    except AttributeError:
        context = {
    }
    return context