from rest_framework import serializers
from .models import Country, Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code', 'name']

class CountrySerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'cca2', 'capital', 'population', 'region', 'timezones', 'flag', 'languages']
