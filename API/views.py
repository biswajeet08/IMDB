import io
from rest_framework.parsers import JSONParser
from .serializer import IMDBSerializer
from .models import IMDB
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAdminUser])
def imdb_api_admin(request):
    if request.method == 'GET':
        name = request.data.get('name')
        if name is not None:
            try:
                movie = IMDB.objects.get(name=name)
                serializer = IMDBSerializer(movie)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                res = {'Error': 'Movie Not Found'}
                return Response(res, status=status.HTTP_404_NOT_FOUND)
        else:
            movies = IMDB.objects.all()
            serializer = IMDBSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        payload = request.data
        serializer = IMDBSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            res = {'message': 'Data Created'}
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        payload = request.data
        name = payload.get('name')
        try:
            movie = IMDB.objects.get(name=name)
            serializer = IMDBSerializer(movie, data=payload, partial=True)
            if serializer.is_valid():
                serializer.save()
                res = {'message': 'Data Updated'}
                return Response(res, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            res = {'Error': 'Movie Not Found'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        payload = request.data
        name = payload.get('name')
        try:
            movie = IMDB.objects.get(name=name)
            movie.delete()
            res = {'Message': 'Movie Deleted'}
            return Response(res, status=status.HTTP_200_OK)
        except:
            res = {'Error': 'Movie Not Found'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def imdb_api_user(request):
    if request.method == 'GET':
        name = request.data.get('name')
        if name is not None:
            try:
                movie = IMDB.objects.get(name=name)
                serializer = IMDBSerializer(movie)
                return Response(serializer.data)
            except:
                res = {'Error': 'Movie Not Found'}
                return Response(res)
        else:
            movies = IMDB.objects.all()
            serializer = IMDBSerializer(movies, many=True)
            return Response(serializer.data)
