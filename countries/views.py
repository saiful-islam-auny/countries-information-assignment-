from rest_framework import viewsets, filters
from .models import Country, Language
from .serializers import CountrySerializer, LanguageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Prefetch


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
    
    @action(detail=True, methods=['get'])
    def same_region(self, request, pk=None):
        try:
            country = self.get_object()
            countries = Country.objects.filter(region=country.region).exclude(id=country.id)
            serializer = self.get_serializer(countries, many=True)
            return Response(serializer.data)
        except Country.DoesNotExist:
            return Response({"detail": "Country not found."}, status=404)


    @action(detail=False, methods=['get'], url_path='by-language-name/(?P<language_name>[^/.]+)')
    def by_language_name(self, request, language_name=None):
        countries = Country.objects.prefetch_related(
            Prefetch('languages', queryset=Language.objects.filter(name__iexact=language_name))
        ).filter(languages__name__iexact=language_name).distinct()

        serializer = self.get_serializer(countries, many=True)
        return Response(serializer.data)


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
