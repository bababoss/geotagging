from django.shortcuts import render
#---------------------Its for function based views-----------------------
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exampt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser

#------------ ---------------------- ---------------- ---------

#---------Usins class based views--------------------
from mapapp.models import GeoData_table

from mapapp.serializers import GeoData_tableSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#import other module
from datetime import datetime
from django.utils import timezone

import time

class GeoData_tableList(APIView):
    """
    List all attendance, or create a new geodata_table.
    """
    def get(self, request,user_id,year,month, format=None):
        geodata_table = GeoData_table.objects.filter(user_id__contains=user_id,created__year=year,created__month=month)
        serializer = GeoData_tableSerializer(geodata_table, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeoData_tableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GeoData_tableDetail(APIView):
    """
    Retrieve, update or delete a geodata_table instance.
    """
    def get_object(self, user_id):
        try:
            return GeoData_table.objects.get(user_id=user_id)
        except GeoData_table.DoesNotExist:
            raise Http404

    def get(self, request, user_id,year, format=None):
        geodata_table = self.get_object(user_id)
        serializer = GeoData_tableSerializer(geodata_table)
        return Response(serializer.data)

    def put(self, request, user_id,year, format=None):
        geodata_table = self.get_object(user_id)
        serializer = GeoData_tableSerializer(geodata_table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id,year, format=None):
        geodata_table = self.get_object(user_id)
        geodata_table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def home(request):

    return render(request,'mapapp/home.html',{})

def index(request):
	
    return render(request,'mapapp/index.html',{})

