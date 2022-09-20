#Handle all the frontend Links
#example: 127.0.0.8000/Classes
from django.urls import path
from .views import index
urlpatterns = [
    path('', index),
]