from django.urls import path
from snippets.views import home, SnippetList, SnippetDetail

urlpatterns = [
    path('', home),
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
]
