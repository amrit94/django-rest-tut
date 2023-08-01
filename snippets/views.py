from django.shortcuts import render
from django.http import HttpResponse

def home(requests):
    html = "<html><body><h1>Welcome</h1></body></html>"
    return HttpResponse(html)