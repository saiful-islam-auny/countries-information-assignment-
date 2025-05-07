from rest_framework import viewsets, filters
from .models import Country, Language
from .serializers import CountrySerializer, LanguageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.paginator import Paginator

# --------------------------------------------------
# CountryViewSet: Handles CRUD operations for countries
# --------------------------------------------------
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    # -------------------------
    # Custom Action: /countries/{id}/regional/
    # Returns countries in the same region excluding self
    # -------------------------
    @action(detail=True, methods=['get'])
    def regional(self, request, pk=None):
        country = self.get_object()
        others = Country.objects.filter(region=country.region).exclude(pk=country.pk)
        serializer = self.get_serializer(others, many=True)
        return Response(serializer.data)
    
    # -------------------------
    # Custom Action: /countries/{id}/same-region/
    # (Duplicate logic with fallback exception handling)
    # -------------------------
    @action(detail=True, methods=['get'])
    def same_region(self, request, pk=None):
        try:
            country = self.get_object()
            countries = Country.objects.filter(region=country.region).exclude(id=country.id)
            serializer = self.get_serializer(countries, many=True)
            return Response(serializer.data)
        except Country.DoesNotExist:
            return Response({"detail": "Country not found."}, status=404)
        
        
    # -------------------------
    # Custom Action: /countries/by-language-name/<language_name>/
    # Assignment Requirement: Filter countries by language name
    # -------------------------
    @action(detail=False, methods=['get'], url_path='by-language-name/(?P<language_name>[^/.]+)')
    def by_language_name(self, request, language_name=None):
        countries = Country.objects.prefetch_related(
            Prefetch('languages', queryset=Language.objects.filter(name__iexact=language_name))
        ).filter(languages__name__iexact=language_name).distinct()

        serializer = self.get_serializer(countries, many=True)
        return Response(serializer.data)

# --------------------------------------------------
# LanguageViewSet: Read-only viewset for language data
# Assignment Requirement: Expose language info via API
# --------------------------------------------------
class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


# ----------------------------------------------------------------------
# FRONTEND, For displaying country data using HTML templates
# ----------------------------------------------------------------------

def country_list(request):
    if not request.user.is_authenticated:
        return redirect('login')   # Redirect to login if not authenticated

    countries = Country.objects.all()

    # Search
    search_query = request.GET.get('search', '')
    if search_query:
        countries = countries.filter(name__icontains=search_query)

    # PAGINATION
    paginator = Paginator(countries, 10)  # Show 10 countries per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'countries/country_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
    })

def country_details(request, id): # Shows detailed info about a selected country (same region, language)
    country = get_object_or_404(Country, pk=id)
    regional_countries = Country.objects.filter(region=country.region).exclude(id=country.id)
    languages = country.languages.all()
    return render(request, 'countries/country_details.html', {
        'country': country,
        'regional_countries': regional_countries,
        'languages': languages,
    })