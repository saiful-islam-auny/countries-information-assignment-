from rest_framework import viewsets, filters
from .models import Country, Language
from .serializers import CountrySerializer, LanguageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render

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



def country_list(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if not authenticated
    
    countries = Country.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        countries = countries.filter(name__icontains=search_query)
    return render(request, 'countries/country_list.html', {'countries': countries})


def country_details(request, id):
    country = get_object_or_404(Country, pk=id)
    regional_countries = Country.objects.filter(region=country.region).exclude(id=country.id)
    languages = country.languages.all()
    return render(request, 'countries/country_details.html', {
        'country': country,
        'regional_countries': regional_countries,
        'languages': languages,
    })