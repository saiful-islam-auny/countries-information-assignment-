# 🌍 Country Information App

This Django-based web application fetches and displays information about countries using the [REST Countries API](https://restcountries.com). It supports user authentication, a searchable web interface, and a RESTful API for country data.

---

## ✅ Features

- Fetch and store country data from an external API (REST Countries)
- User registration and login system
- Search countries by name
- View countries in the same region
- Filter countries by language
- RESTful API (with Django REST Framework)
- PostgreSQL as the database
- Data preloaded via `data.json` (if preferred over live fetching)

---

## 🚀 Setup Instructions

### 1. 📦 Installation

```bash
git clone https://github.com/saiful-islam-auny/countries-information-assignment-.git
cd country-information

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For Linux/macOS
# or
venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt
