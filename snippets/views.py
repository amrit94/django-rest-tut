from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
import io


def home(requests):
    html = "<html><body><a href='/snippets/'>Snippet</a><br><a href='/snippets/1/'>Snippet-1</a></body></html>"
    return HttpResponse(html)


# python manage.py shell
# Serializing of one instances
"""
# # 1. Translated the model instance into Python native datatypes
serializer = SnippetSerializer(Snippet.objects.all())
serializer.data
#  {'language': 'python', 'style': 'friendly'}
# # 2. Then render the data into json
content = JSONRenderer().render(serializer.data)
content
# b'{"language":"python","style":"friendly"}'
"""


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    # Serialize querysets
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        # To serialize a queryset or list of objects instead of a single object instance use `many=True`
        return JsonResponse(serializer.data, safe=False)  # JsonResponse --> serialized to JSON
        # By defaults `safe=True` --> to serialized Dict obj
        # safe=False --> to serialized Non-Dict obj

    # Deserialization
    elif request.method == 'POST':
        """# Postman --> body-raw-text
        {"title": "Lang3", "language": "python", "style": "friendly"} """
        # 1. First  parse a stream into Python native datatypes
        data = JSONParser().parse(request)
        # 2. Then we restore those native datatypes into a fully populated object instance.
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():  # uses all the validation of models
            serializer.save()  # call creates methods
            return JsonResponse(serializer.data, status=201)  # 201 - successfully created an object
        return JsonResponse(serializer.errors, status=400)  # 400 - Bad request


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return JsonResponse({"error": "question not found "}, status=404)

        # Serializing of one instances
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)  # Model instance(single obj) so many=True not req
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        """# Postman --> body-raw-text
           {"title": "Lang10", "language": "python", "style": "friendly"} """
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)  # snippet = old fields value, N data = updated fields value
        # In PUT we need to pass all fields
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return JsonResponse({'Success': "Data deleted"})
