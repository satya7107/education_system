
from django.http import HttpResponse
from watchlist.api.serializers import movieserializer
from rest_framework.response import Response
from watchlist.models import movie
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET', 'POST'])
def allmovies(request):
    if request.method=='GET':
        movies=movie.objects.all()
        serializer=movieserializer(movies,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=movieserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status="HTTP_404_NOT_FOUND")
@api_view(['GET', 'PUT', 'DELETE'])
def movielist(request,pk):
    if request.method=='GET':
        movies=get_object_or_404(movie,pk=pk)
        serializer=movieserializer(movies)
        return Response(serializer.data)
    if request.method=='PUT':
        mymovies=get_object_or_404(movie,pk=pk)
        serializer=movieserializer(mymovies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status="HTTP_404_NOT_FOUND")
        

    if request.method == 'DELETE':
        movies=get_object_or_404(movie,pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


