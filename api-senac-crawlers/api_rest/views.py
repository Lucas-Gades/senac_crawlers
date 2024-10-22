from rest_framework import status
from rest_framework.response import Response
from .models import Edital, Site, Usuario
from .serializers import EditalSerializer, SiteSerializer, UsuarioSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse

def home(request):
    return HttpResponse("Seja bem-vindo à API Senac Crawlers! :))")

# CRUD Edital

# INSERIR E BUSCAR EDITAL
@api_view(['GET', 'POST'])
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

# DELETAR EDITAL POR ID
@api_view(['DELETE', 'GET'])
def edital_delete(request, pk):
    try:
        edital = Edital.objects.get(pk=pk)

        if request.method == 'GET':
            # Retorna as informações do edital
            serializer = EditalSerializer(edital)
            return Response({"edital": serializer.data}, status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            # Deleta o edital
            edital.delete()
            return Response({"message": "Edital deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)

    except Edital.DoesNotExist:
        return Response({"message": "Edital não encontrado."}, status=status.HTTP_404_NOT_FOUND)

#ATUALIZAR EDITAL POR ID
@api_view(['GET', 'PUT'])
def edital_update(request, pk):
    try:
        edital = Edital.objects.get(pk=pk)

        if request.method == 'GET':
            # Retorna as informações do edital
            serializer = EditalSerializer(edital)
            return Response({"edital": serializer.data}, status=status.HTTP_200_OK)

        if request.method == 'PUT':
            # Atualiza as informações do edital
            serializer = EditalSerializer(edital, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Edital atualizado com sucesso!", "edital": serializer.data})
            return Response({"message": "Erro ao atualizar edital.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    except Edital.DoesNotExist:
        return Response({"message": "Edital não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    

# CRUD Site

# INSERIR E BUSCAR SITE
@api_view(['GET', 'POST'])
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

# DELETAR SITE POR ID
@api_view(['DELETE', 'GET'])
def site_delete(request, pk):
    try:
        site = Site.objects.get(pk=pk)

        if request.method == 'GET':
            # Retorna as informações do site
            serializer = SiteSerializer(site)
            return Response({"site": serializer.data}, status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            # Deleta o site
            site.delete()
            return Response({"message": "Site deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)

    except Site.DoesNotExist:
        return Response({"message": "Site não encontrado."}, status=status.HTTP_404_NOT_FOUND)

#ATUALIZAR SITE POR ID
@api_view(['PUT', 'GET'])
def site_update(request, pk):
    try:
        site = Site.objects.get(pk=pk)
    except Site.DoesNotExist:
        return Response({"message": "Site não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retorna as informações do site
        serializer = SiteSerializer(site)
        return Response({"site": serializer.data}, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        # Atualiza as informações do site
        serializer = SiteSerializer(site, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Site atualizado com sucesso!", "data": serializer.data})
        return Response({"message": "Erro ao atualizar site.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# CRUD Usuario

# INSERIR E BUSCAR USUARIO
@api_view(['GET', 'POST'])
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

# DELETAR USUARIO POR ID
@api_view(['DELETE', 'GET'])
def usuario_delete(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)

        if request.method == 'GET':
            # Retorna as informações do usuário
            serializer = UsuarioSerializer(usuario)
            return Response({"usuario": serializer.data}, status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            # Deleta o usuário
            usuario.delete()
            return Response({"message": "Usuário deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)

    except Usuario.DoesNotExist:
        return Response({"message": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

#ATUALIZAR USUARIO POR ID
@api_view(['PUT', 'GET'])
def usuario_update(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)

        if request.method == 'GET':
            # Retorna as informações do usuário
            serializer = UsuarioSerializer(usuario)
            return Response({"usuario": serializer.data}, status=status.HTTP_200_OK)

        if request.method == 'PUT':
            # Atualiza as informações do usuário
            serializer = UsuarioSerializer(usuario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Usuário atualizado com sucesso!", "data": serializer.data})
            return Response({"message": "Erro ao atualizar usuário.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    except Usuario.DoesNotExist:
        return Response({"message": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
