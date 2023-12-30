
from django.urls import path 
from .views import watch , delete
urlpatterns = [
    path('watch', watch, name='watch'),
    path('delete', delete, name='delete')
]
