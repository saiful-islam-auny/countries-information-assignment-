from rest_framework import serializers
from .models import Country, Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code', 'name']

class CountrySerializer(serializers.ModelSerializer):
    # For writing (POST/PUT)
    language_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Language.objects.all(),
        write_only=True,
        source='languages'
    )

    # For reading (GET)
    languages = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = [
            'id', 'name', 'cca2', 'capital', 'population', 'region',
            'timezones', 'flag', 'languages', 'language_ids'
        ]
