from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser
from api.models import VersionModel
from api.serializers import BalconySerializer


class Version(APIView):
    def get(self, request):
        return Response(VersionModel(0, 0, 1).json())


class Balcony(APIView):

    def post(self, request):
        serializer = BalconySerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KPI(APIView):

    def post(self, request):
        return Response("Nothing to see here!")
