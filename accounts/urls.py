from django.urls import path,re_path
from accounts.views import register,login,logout


app_name='accounts'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

]