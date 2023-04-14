from django.urls import path
from index.views import home ,instagram_bot,add_instagram

app_name='index'
urlpatterns = [
    path('', home, name='home'),
    path('instagram/', instagram_bot, name='instagram'),
    path('add_instagram/', add_instagram, name='add_instagram'),
]

