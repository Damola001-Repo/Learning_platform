from django.contrib import admin
from .models import Course, WhatYouWillLearn, Section, Lecture, Project, Enrollment, Topic, Instructor, Student
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(WhatYouWillLearn)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lecture)
admin.site.register(Project)
admin.site.register(Enrollment)
admin.site.register(Topic)
admin.site.register(Instructor)
admin.site.register(Student)