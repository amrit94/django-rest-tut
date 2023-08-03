from django.http import HttpResponse
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins, generics


def home(requests):
    html = "<html><body><a href='/snippets/'>Snippet</a><br><a href='/snippets/1/'>Snippet-1</a></body></html>"
    return HttpResponse(html)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
