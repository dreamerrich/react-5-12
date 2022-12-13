from django.shortcuts import render
from .Serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def detailView(request):
    if request.method == 'GET':
        data = Form.objects.all()

        serializer = FormSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def data_detail(request, pk):
    try:
        datadetail = Form.objects.get(pk=pk)
    except Form.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FormSerializer(datadetail)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FormSerializer(datadetail, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        datadetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  