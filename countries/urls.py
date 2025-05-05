from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, LanguageViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'languages', LanguageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('countries/<int:pk>/same-region/', CountryViewSet.as_view({'get': 'same_region'})),
    path('countries/by-language-name/<str:language_name>/', CountryViewSet.as_view({'get': 'by_language_name'})),
]


from .views import country_list_view, country_details_view

urlpatterns += [
    path("countries-page/", country_list_view, name="countries_page"),
    path("country/<int:pk>/details/", country_details_view, name="country_details"),
]
