from django.urls import path
from snippets.views import home, snippet_list, snippet_detail

urlpatterns = [
    path('', home),
    path('snippets/', snippet_list),
    path('snippets/<int:pk>/', snippet_detail),
]
