from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Objetivo, Post, Corazones, SesionEnfoque
from django.db.models import Q
from .serializer import ObjetivoSerializer, PostSerializer, SesionEnfoqueSerializer, CorazonesSerializer
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
def get_estadisticas(request, pk):
    objetivos=Objetivo.objects.filter(id_autor_id=pk)
    total=objetivos.count()
    total_completado= objetivos.filter(completado=True).count()
    apoyo_recibido = Corazones.objects.aggregate(total=Count('id',
            filter=Q(id_post__id_autor__id=pk, corazon=True)))
    personas_que_has_inspirado = Corazones.objects.aggregate(total=Count('id_post_id',
            filter=Q(id_autor=pk, corazon=True), distinct=True))
    formato={"Total de Objetivos":total,
             "Total de Completados": total_completado,
             "Apoyo recibido": apoyo_recibido["total"],
             "Personas que has inspirado": personas_que_has_inspirado["total"]}
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

# Vistas
@api_view(['GET'])
def get_sesion_enfoque(request, pk):
    try:
        sesion = SesionEnfoque.objects.get(pk=pk)
    except SesionEnfoque.DoesNotExist:
        return Response({"error": "No se ha encontrado la sesión con esa llave primaria"},
                        status=status.HTTP_404_NOT_FOUND)

    serializer = SesionEnfoqueSerializer(sesion)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_sesion_enfoque(request):
    sesiones = SesionEnfoque.objects.all()
    serializer = SesionEnfoqueSerializer(sesiones, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_sesion_enfoque(request):
    serializer = SesionEnfoqueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_sesion_enfoque(request, pk):
    try:
        sesion = SesionEnfoque.objects.get(pk=pk)
    except SesionEnfoque.DoesNotExist:
        return Response({"error": "No se ha encontrado la sesión con esa llave primaria"},
                        status=status.HTTP_404_NOT_FOUND)
    sesion.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
def put_sesion_enfoque(request, pk):
    try:
        sesion = SesionEnfoque.objects.get(pk=pk)
    except SesionEnfoque.DoesNotExist:
        return Response({"error": "No se ha encontrado la sesión con esa llave primaria"},
                        status=status.HTTP_404_NOT_FOUND)

    serializer = SesionEnfoqueSerializer(sesion, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_corazon(request, pk):
    try:
        corazon = Corazones.objects.get(pk=pk)
    except Corazones.DoesNotExist:
        return Response({"error": "No se ha encontrado el registro con esa llave primaria"},
                        status=status.HTTP_404_NOT_FOUND)

    serializer = CorazonesSerializer(corazon)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_corazones(request):
    corazones = Corazones.objects.all()
    serializer = CorazonesSerializer(corazones, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_corazon(request):
    serializer = CorazonesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_corazon(request, pk):
    try:
        corazon = Corazones.objects.get(pk=pk)
    except Corazones.DoesNotExist:
        return Response({"error": "No se ha encontrado el registro con esa llave primaria"},
                        status=status.HTTP_404_NOT_FOUND)
    corazon.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
def put_corazon(request, pk):
    try:
        corazon = Corazones.objects.get(pk=pk)
    except Corazones.DoesNotExist:
        return Response({"error": "No se ha encontrado el registro con esa llave primaria"},
                        status=status.HTTP_404_NOT_FOUND)

    serializer = CorazonesSerializer(corazon, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

