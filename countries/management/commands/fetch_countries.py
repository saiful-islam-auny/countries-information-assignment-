# ----------------------------------------------------------------------
# Django Management Command: fetch_countries
# ----------------------------------------------------------------------

import requests
from django.core.management.base import BaseCommand
from countries.models import Country, Language

class Command(BaseCommand):
    help = "Fetch countries from REST Countries API and store them in the database"

    def handle(self, *args, **options):  # Step 1: Fetch country data from the API
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Failed to fetch data"))
            return

        data = response.json()
        
        # --------------------------------------------
        # Step 2: Loop through each country entry
        # --------------------------------------------
        for item in data:
            name = item.get("name", {}).get("common")
            cca2 = item.get("cca2")
            capital = item.get("capital", [""])[0] if item.get("capital") else ""
            population = item.get("population", 0)
            region = item.get("region", "")
            timezones = item.get("timezones", [])
            flag = item.get("flags", {}).get("png", "")

            country, created = Country.objects.get_or_create( # Step 3: Create Country if not already exists
                cca2=cca2,
                defaults={
                    "name": name,
                    "capital": capital,
                    "population": population,
                    "region": region,
                    "timezones": timezones,
                    "flag": flag,
                }
            )

            if not created:
                continue  # Skip if already exists

            langs = item.get("languages", {}) # Step 4: Handle Many-to-Many Language Relations
            for code, lang_name in langs.items():
                language, _ = Language.objects.get_or_create(code=code, defaults={"name": lang_name})
                country.languages.add(language)

            self.stdout.write(self.style.SUCCESS(f"Saved country: {name}")) #Step 5: Output success message for saved country
