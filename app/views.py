from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuarioSerializer
# Create your views here.


@api_view(['GET'])
def pegar_usuario(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def pegar_apelido(request, apelido):
    try:
        usuario = Usuario.objects.get(pk=apelido)

    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def gerenciar_usuario(request):
    if request.method == 'GET':
        apelido = request.query_params.get('usuario')
        if apelido:
            try:
                usuario = Usuario.objects.get(pk=apelido)

            except Usuario.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        apelido = request.data.get('apelido_usuario')
        try:
            usuario = Usuario.objects.get(pk=apelido)

        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        apelido = request.data.get('apelido_usuario')
        try:
            usuario = Usuario.objects.get(pk=apelido)

        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
