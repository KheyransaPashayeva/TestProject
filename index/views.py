from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index/index.html')


def instagram_bot(request):
    return render(request, 'instagram/instagram.html')

def add_instagram(request):
    return render(request, 'instagram/instagram_login.html')
