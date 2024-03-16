from django.urls import path

from .views import (
    message
)

urlpatterns = [
    path('', message, name='message')
    
]
