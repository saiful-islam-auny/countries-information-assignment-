# 🌍 Country Information App

This Django-based web application fetches and displays information about countries using the [REST Countries API](https://restcountries.com/v3.1/all). It supports user authentication, a searchable web interface, and a RESTful API for country data.

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
```

---

## 2. ⚙️ Dependencies

The project relies on the following key packages:

- **Django==4.2**
- **djangorestframework==3.14.0**
- **psycopg2-binary==2.9.9** – PostgreSQL adapter
- **requests==2.31.0** – To fetch country data from external API
- **Bootstrap (via CDN)** – Used for frontend styling

> All dependencies are listed in the `requirements.txt` file.

---

## 3. 🛠️ Database Setup (PostgreSQL)

Make sure PostgreSQL is installed and running.

### Create Database:

```sql
# Log into PostgreSQL
psql -U postgres

-- Create the database
CREATE DATABASE "country-db";

-- (Optional) Create a new user if you don’t want to use 'postgres'
CREATE USER myuser WITH PASSWORD 'mypassword';

-- (Optional) Grant privileges
GRANT ALL PRIVILEGES ON DATABASE "country-db" TO myuser;

-- Exit the shell
\q
```
### Configure `settings.py`:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'country-db',
        'USER': 'postgres',        # Change if needed
        'PASSWORD': '1234',        # Change if needed
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 4.🧱 Migrations & Data Load:
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate
```
### Fetch data from REST API
```bash
python manage.py fetch_countries  #This will call the REST Countries API and populate the database with real-time data.
```

---

## 5. 👤 Create Superuser (for admin access)
```bash
python manage.py createsuperuser
```
### 6. 🚦 Run the Development Server
```bash
python manage.py runserver
```
### Then go to http://127.0.0.1:8000 in your browser.

---

## 🔑 Key Endpoints

Here are the key API endpoints for the project:

### 1. `/api/countries/`
- **Method**: `GET`
- **Description**: Returns a list of all countries.
- **Query Parameters**: `search` (optional) - Search for a country by name.

- **Method**: `POST`
- **Description**: Create a new country. Requires authentication and valid language IDs.

### 2. `/api/countries/{id}/`
- **Method**: `GET`
- **Description**: Get details of a specific country by `id`.

- **Method**: `PUT` / `PATCH`
- **Description**: Update a specific country's details.

- **Method**: `DELETE`
- **Description**: Delete a specific country.

### 3. `/api/countries/{id}/same-region/`
- **Method**: `GET`
- **Description**: Get countries from the same region as the specified country.

### 4. `/api/countries/{id}/regional/`
- **Method**: `GET`
- **Description**: Another custom action to retrieve countries in the same region.

### 5. `/api/countries/by-language-name/{language_name}/`
- **Method**: `GET`
- **Description**: Get a list of countries that speak the specified language.

### 6. `/api/languages/`
- **Method**: `GET`
- **Description**: Get a list of all languages in the database.

---

## 🗃️ Project Structure Overview
```bash
country_information/
├── accounts/           # Authentication app
├── countries/          # Country & language models and views
├── templates/          # HTML templates
├── data.json           # Preloaded sample data
├── manage.py
├── requirements.txt
└── README.md
```
---

## 📞 Contact

For any questions, feedback, or follow-ups, feel free to reach out via:

- Email: [aunychowdhury99@gmail.com](mailto:aunychowdhury99@gmail.com)
- LinkedIn: [Saiful Islam Auny](https://www.linkedin.com/in/saiful-islam-auny/)
