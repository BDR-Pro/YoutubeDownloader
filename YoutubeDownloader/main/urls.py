
from django.urls import path 
from .views import download , delete ,  main , video_details
urlpatterns = [
    path('download',download, name='download'),
    path('watch', main, name='watch'),
    path('delete', delete, name='delete'),
    path('video_details/', video_details, name='video_details'),

]
