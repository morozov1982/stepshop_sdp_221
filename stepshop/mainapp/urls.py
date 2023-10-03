from django.urls import path

from mainapp.views import index, about

urlpatterns = [
    path('', index),
    path('about/', about),
]
