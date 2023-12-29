
from django.urls import path 
from .views import watch
urlpatterns = [
    path('watch', watch, name='watch')
]
