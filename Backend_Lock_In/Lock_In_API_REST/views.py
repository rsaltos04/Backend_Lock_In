from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Objetivo, Post
from .serializer import ObjetivoSerializer, PostSerializer
from django.db.models import Count

# Create your views here.

# Vistas de objetivos
@api_view(['GET'])
def get_objetivo(request,pk):
    
    try:
        objetivo=Objetivo.objects.get(pk=pk)
    except Objetivo.DoesNotExist:
        return Response({"error":"No se ha encontrado el objetivo con esa llave primaria"},status.HTTP_400_BAD_REQUEST)
    
    serializer=ObjetivoSerializer(objetivo)
    return Response(serializer.data)

@api_view(['GET'])
def get_objetivo_estadistico(request, pk):
    objetivos=Objetivo.objects.filter(id_autor_id=pk)
    total=objetivos.count()
    total_completado= objetivos.filter(completado=True).count()
    porcentaje= (total_completado/total)*100
    formato={"Total de Objetivos":total,
             "Total de Completados": total_completado,
             "Porcentaje de Objetivos completados": porcentaje}
    return Response(formato,status.HTTP_200_OK)

@api_view(['GET'])
def get_all_objetivo(request):
    objetivos=Objetivo.objects.all()
    serializer=ObjetivoSerializer(objetivos,many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def create_objetivo(request):
    serializer= ObjetivoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_objetivo(request, pk):
    try:
        objetivo=Objetivo.objects.get(pk=pk)
    except Objetivo.DoesNotExist:
        return Response({"error":"No se ha encontrado el objetivo con esa llave primaria"},status.HTTP_400_BAD_REQUEST)
    objetivo.delete()
    return Response(status.HTTP_200_OK)

@api_view(['PUT'])
def put_objetivo(request, pk):
    try:
        objetivo=Objetivo.objects.get(pk=pk)
    except Objetivo.DoesNotExist:
        return Response({"error":"No se ha encontrado el objetivo con esa llave primaria"},status.HTTP_400_BAD_REQUEST)
    serializer=ObjetivoSerializer(objetivo,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

# Vista de post
@api_view(['GET'])
def get_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"error": "No se ha encontrado el objetivo con esa llave primaria"},
                        status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_post(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request, pk):
    try:
        post=Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"error":"No se ha encontrado el objetivo con esa llave primaria"},status.HTTP_400_BAD_REQUEST)
    post.delete()
    return Response(status.HTTP_200_OK)

@api_view(['PUT'])
def put_post(request, pk):
    try:
        post=Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"error":"No se ha encontrado el objetivo con esa llave primaria"},status.HTTP_400_BAD_REQUEST)
    serializer=PostSerializer(post,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)