from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import Version

# Create your views here.


def version(request):
    return JsonResponse(Version().json(), safe=False)
