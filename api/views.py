from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Version


@api_view(['GET'])
def version(request):
    return Response(Version(0, 0, 1).json())


@api_view(['POST'])
def balcony(request):
    return Response("Nothing to see here!")


@api_view(['POST'])
def kpi(request):
    return Response("Nothing to see here!")
