from django.contrib import admin
from django.urls import path, include
from accounts.views import landing
from countries.views import country_list, country_details

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # -------------------------------
    # REST API Endpoints
    # -------------------------------
    path('api/', include('countries.urls')), # country-related API routes
    path('accounts/', include('accounts.urls')),  # Routes for user registration and login (assignment requirement)
    path('', landing, name='landing'),  # Displays a public home/landing page
    path('countries/', country_list, name='country_list'),  # Country list page
    path('countries/<int:id>/details/', country_details, name='country_details'),  # Country details page
]
