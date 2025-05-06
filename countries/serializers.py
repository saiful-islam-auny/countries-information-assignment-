from rest_framework import serializers
from .models import Country, Language

# -------------------------------
# Language Serializer
# -------------------------------
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code', 'name']


# -------------------------------
# Country Serializer
# -------------------------------
class CountrySerializer(serializers.ModelSerializer):
    # Write-only field to accept language IDs when creating/updating countries (POST/PUT)
    language_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Language.objects.all(),
        write_only=True,
        source='languages' # Maps to ManyToManyField on the model
    )

    # For reading (GET)
    languages = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = [
            'id', 'name', 'cca2', 'capital', 'population', 'region', 
            'timezones', 'flag', 'languages', 'language_ids' # Both readable and writable fields
        ]
