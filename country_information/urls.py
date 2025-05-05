from django.contrib import admin
from django.urls import path, include
from accounts.views import landing
from countries.views import country_list, country_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('countries.urls')),
    path('accounts/', include('accounts.urls')),  # Ensure this line is included
    path('', landing, name='landing'),  # Landing page
    path('countries/', country_list, name='country_list'),  # Country list page
    path('countries/<int:id>/details/', country_details, name='country_details'),  # Country details page
]
