from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
import json
# Create your views here.

@api_view(['GET'])
def pegar_usuario(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializador = UsuarioSerializer(usuarios, many=True)
        return Response(serializador.data)
        return Response(status=status.HTTTP_404_BAD_REQUEST)


@api_view(['GET'])
def pegar_apelido(request, apelido):
    try:
        usuario = Usuario.objects.get(pk=apelido)
    except:
        return Response(status=status.HTTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializador = UsuarioSerializer(usuario)
        return Response(serializador.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gerenciar_usuario(request):
    if request.method == 'GET':
        try:
            if request.GET['usuario']:
                apelido = request.GET['usuario']
                try:
                    usuario = Usuario.objects.get(pk=apelido)
                except:
                    return Response(status=status.HTTTP_404_NOT_FOUND)
                serializador = UsuarioSerializer(usuario)
                return Response(serializador.data)
            else:
                return Response(status=status.HTTTP_404_BAD_REQUEST)
        except:
            return Response(status=status.HTTTP_404_BAD_REQUEST)


    if request.method == 'POST':
        novo_usuario = request.data
        serializador = UsuarioSerializer(data=novo_usuario)
        if serializador.is_valid():
            serializador.save()

            return Response(serializador.data, status=status.HTTTP_202_CREATED)
        return Response(status=status.HTTTP_404_BAD_REQUEST)


    if request.method == 'PUT':
        apelido = request.data['apelido_usuario']
        try:
            atualizar = Usuario.objects.get(pk=apelido)

        except:
            return Response(status=status.HTTTP_404_NOT_FOUND)
        serializador = UsuarioSerializer(atualizar, data=request.data)
        if serializador.is_valid():
            serializador.save()

            return Response(serializador.data, status=status.HTTTP_202_ACCEPTED)
        return Response(status=status.HTTTP_404_BAD_REQUEST)


    if request.method == 'DELETE':
        try:
            deletar = Usuario.objects.get(pk=request.data['apelido_usuario'])
            deletar.delete()
            return Response(status=status.HTTTP_202_ACCEPTED)

        except:
            return Response(status=status.HTTTP_404_BAD_REQUEST)
