from .models import Course, CustomUser, WhatYouWillLearn, Section, Lecture, Topic, Student, Enrollment, Instructor
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.db.models import Q


# Create your views here.

# @login_required(login_url='login')
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except:
            messages.error(request, "User doest not exist")
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Invalid username or password")

    context = {
        'page':page
    }

    return render(request, 'base/login_register.html', context=context)



def logoutUser(request):
    logout(request)
    return redirect('home')



def registerUser(request):
    form = CustomUserCreationForm()

    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER'))
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            messages.error(request, "Something went wrong while trying to register user")

    return render(request, 'base/login_register.html', {'form':form})
    


def homePage(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    courses = Course.objects.filter(
        Q(title__icontains=q) | Q(description__icontains=q) | Q(instructor__first_name__icontains=q) | Q(instructor__last_name__icontains=q)
    )

    paginator = Paginator(courses, 24)
    page_number = request.GET.get('page')

    courses = paginator.get_page(page_number)

    context = {
        'courses': courses
    }

    return render(request, 'base/home.html', context)



def navbar(request):

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
        
    return render(request, 'base/navbar.html', context)



def coursesPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    courses = Course.objects.filter(
        Q(title__icontains=q) | Q(description__icontains=q) | Q(instructor__first_name__icontains=q) | Q(instructor__last_name__icontains=q)
    )

    context = {
        'courses': courses
    }

    return render(request, 'base/courses.html', context)



def courseDetails(request, pk):
    course = Course.objects.get(pk=pk)
    learning = course.learning.all()
    sections = course.sections.all()
    sections_with_topics = []

    for section in sections:
        topics = section.topic.all()  # Using the related_name 'topic'
        projects = section.projects.all()
        sections_with_topics.append({
            'section': section,
            'topics': topics,
            'projects': projects
        })

    context = {
        'course':course,
        'learning':learning,
        'sections_with_topics': sections_with_topics,
        'topics': topics
    }
    return render(request, 'base/course-details.html', context)



@login_required(login_url='login')
def profile(request):

    user = request.user
    student_email = user.student
    student = Student.objects.get(user__email=student_email)
    enrolled_courses = Enrollment.objects.filter(student=student).select_related('course', 'course__instructor')


    context = {
        'user': user,
        'student': student,
        'enrolled_courses': enrolled_courses
    }

    return render(request, 'base/profile.html', context)



@login_required(login_url='login')
def payment(request):
    return render(request, 'base/payment.html', {})