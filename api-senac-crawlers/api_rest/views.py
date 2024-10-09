from rest_framework import status
from rest_framework.response import Response
from .models import Edital, Site, Usuario
from .serializers import EditalSerializer, SiteSerializer, UsuarioSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse

def home(request):
    return HttpResponse("Seja bem-vindo à API Senac Crawlers! :))")

# CRUD para Edital
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def edital_list(request):
    if request.method == 'GET':
        editais = Edital.objects.all()
        serializer = EditalSerializer(editais, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EditalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Edital inserido com sucesso!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Erro ao inserir edital.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        edital_id = request.data.get('id')
        try:
            edital = Edital.objects.get(pk=edital_id)
            serializer = EditalSerializer(edital, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Edital atualizado com sucesso!", "data": serializer.data})
            return Response({"message": "Erro ao atualizar edital.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Edital.DoesNotExist:
            return Response({"message": "Edital não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        edital_id = request.data.get('id')
        try:
            edital = Edital.objects.get(pk=edital_id)
            edital.delete()
            return Response({"message": "Edital deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Edital.DoesNotExist:
            return Response({"message": "Edital não encontrado."}, status=status.HTTP_404_NOT_FOUND)

# CRUD para Site
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def site_list(request):
    if request.method == 'GET':
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Site inserido com sucesso!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Erro ao inserir site.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        site_id = request.data.get('id')
        try:
            site = Site.objects.get(pk=site_id)
            serializer = SiteSerializer(site, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Site atualizado com sucesso!", "data": serializer.data})
            return Response({"message": "Erro ao atualizar site.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Site.DoesNotExist:
            return Response({"message": "Site não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        site_id = request.data.get('id')
        try:
            site = Site.objects.get(pk=site_id)
            site.delete()
            return Response({"message": "Site deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Site.DoesNotExist:
            return Response({"message": "Site não encontrado."}, status=status.HTTP_404_NOT_FOUND)

# CRUD para Usuario
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def usuario_list(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário inserido com sucesso!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Erro ao inserir usuário.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        usuario_id = request.data.get('id')
        try:
            usuario = Usuario.objects.get(pk=usuario_id)
            serializer = UsuarioSerializer(usuario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Usuário atualizado com sucesso!", "data": serializer.data})
            return Response({"message": "Erro ao atualizar usuário.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Usuario.DoesNotExist:
            return Response({"message": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        usuario_id = request.data.get('id')
        try:
            usuario = Usuario.objects.get(pk=usuario_id)
            usuario.delete()
            return Response({"message": "Usuário deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Usuario.DoesNotExist:
            return Response({"message": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
