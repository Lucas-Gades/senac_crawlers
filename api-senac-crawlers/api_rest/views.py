from rest_framework import generics, status
from rest_framework.response import Response
from .models import Edital, Site, Usuario
from .serializers import EditalSerializer, SiteSerializer, UsuarioSerializer

# CRUD para Edital
class EditalListCreate(generics.ListCreateAPIView):
    queryset = Edital.objects.all()
    serializer_class = EditalSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Edital inserido com sucesso!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Erro ao inserir edital.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EditalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Edital.objects.all()
    serializer_class = EditalSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# CRUD para Site
class SiteListCreate(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Site inserido com sucesso!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Erro ao inserir site.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# CRUD para Usuario
class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuário inserido com sucesso!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Erro ao inserir usuário.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
