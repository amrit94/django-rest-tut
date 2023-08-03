from django.http import HttpResponse
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status



def home(requests):
    html =  """<html><body>
                <a href='/snippets/'>Snippet</a><br>
                <a href='/snippets/1/'>Snippet-1</a><br>
                <a href='/simple/snippets/'>Simple Router</a><br>
                <a href='/default/'>Default Router</a><br>
                <a href='/modelviewset/'>Model Viewset</a><br>
                <a href='/ro_viewset/'>Readonly Viewset</a>
            </body></html>"""
    return HttpResponse(html)


# # # 1. ViewSet
class SnippetViewSet(viewsets.ViewSet):
    def list(self, request):
        snippet = Snippet.objects.all()
        serializer = SnippetSerializer(snippet, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get Model instance
    def get_object(self, pk):
        queryset = Snippet.objects.all()
        snippet = get_object_or_404(queryset, pk=pk)
        return snippet

    def retrieve(self, request, pk=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def update(self, request, pk=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# # # 2. ModelViewSets
class SnippetModelViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
# # # 2. ReadOnlyModelViewSet
class SnippetReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer