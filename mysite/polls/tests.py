from django.test import TestCase
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your tests here.
