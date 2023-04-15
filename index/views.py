from django.shortcuts import render,redirect
from .forms import UserForm
from task import instabot

# Create your views here.
def home(request):
    return render(request, 'index/index.html')


def instagram_bot(request):
    return render(request, 'instagram/instagram.html')


def add_instagram(request):
    from accounts.models import InstagramUser,InstagramFollow
    form = UserForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = InstagramUser.objects.filter(username=username).first()
            instabot('https://www.instagram.com', username, password)            
            data = InstagramFollow.objects.filter(user_id=user).first()
            context = {'data': data,
                       'user':user
                       }
            return render(request, 'instagram/instagram.html', context)
    return render(request, 'instagram/instagram_login.html', context)