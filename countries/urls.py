# ---------------------------------------------------------
# URL ROUTING for Country and Language API Endpoints
# ---------------------------------------------------------

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, LanguageViewSet

# ---------------------------------------------------------
# Registering ViewSets with DRF Router
# ---------------------------------------------------------
router = DefaultRouter() # for list, retrieve, create, update, delete
router.register(r'countries', CountryViewSet)
router.register(r'languages', LanguageViewSet)


# ---------------------------------------------------------
# Custom Routes for Additional Filtering Features
# ---------------------------------------------------------
urlpatterns = [
    path('', include(router.urls)),
    path('countries/<int:pk>/same-region/', CountryViewSet.as_view({'get': 'same_region'})),
    path('countries/by-language-name/<str:language_name>/', CountryViewSet.as_view({'get': 'by_language_name'})),
]
