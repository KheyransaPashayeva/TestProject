from django.urls import path
from index.views import home ,instagram_bot

app_name='index'
urlpatterns = [
    path('', home, name='home'),
    path('instagram/', instagram_bot, name='instagram'),
]

