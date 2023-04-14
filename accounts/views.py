from email import message
from django.contrib import messages
from django.conf import settings
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate, get_user_model, login as django_login, logout as django_logout
User = get_user_model()

# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method =='POST':
        form = RegistrationForm(data=request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = False
            user.save()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                django_login(request, user)
                messages.success(request, 'You logged in')
                return redirect(reverse_lazy('index:home'))
            messages.error(request, 'Your credentials are invalid')
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('accounts:login'))