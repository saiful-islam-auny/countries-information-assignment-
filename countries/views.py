from rest_framework import viewsets, filters
from .models import Country, Language
from .serializers import CountrySerializer, LanguageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def regional(self, request, pk=None):
        country = self.get_object()
        others = Country.objects.filter(region=country.region).exclude(pk=country.pk)
        serializer = self.get_serializer(others, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='by-language/(?P<lang_code>[^/.]+)')
    def by_language(self, request, lang_code=None):
        countries = Country.objects.filter(languages__code=lang_code)
        serializer = self.get_serializer(countries, many=True)
        return Response(serializer.data)

class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
