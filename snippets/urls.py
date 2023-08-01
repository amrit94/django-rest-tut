from django.urls import path
from snippets.views import home

urlpatterns = [
    path('', home)
]