# api_rest/serializers.py
from rest_framework import serializers
from .models import Edital, Site, Usuario

class EditalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edital
        fields = '__all__'

    def validate_valor(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("O valor não pode ser negativo.")
        return value


    def validate_img_logo(self, value):
        if value and not value.endswith(('.png', '.jpg', '.jpeg')):
            raise serializers.ValidationError("A imagem do logo deve ser um arquivo .png, .jpg ou .jpeg.")
        return value

    # Adicione mais validações conforme necessário para outros campos

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

    def validate_url(self, value):
        if not value or not value.startswith("http"):
            raise serializers.ValidationError("A URL deve ser válida e começar com 'http'.")
        return value


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


    def validate_email(self, value):
        if not value or '@' not in value:
            raise serializers.ValidationError("O e-mail deve ser um endereço válido.")
        return value
