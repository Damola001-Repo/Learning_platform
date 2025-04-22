from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views import View

# Create your views here.
class UserRegistrationView(View):
    template_name = 'user/register.html'
    form_class = CustomUserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render('login')
        return render(request, self.template_name, {'form': form})