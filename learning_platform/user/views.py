<<<<<<< HEAD
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {first_name}!')
            return redirect('login')  # Redirect to login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html')
=======
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
>>>>>>> 53dee7202975b4351683cf584b71b9914ad1ba55
