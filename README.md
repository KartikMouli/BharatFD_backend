# FAQ Project

This project provides an API for managing FAQs (Frequently Asked Questions) with translations into multiple languages using Django, `django-rest-framework`, `googletrans`, and `ckeditor`. The FAQ can be translated into Hindi and Bengali, with automatic caching of translations for improved performance.

## Table of Contents
1. [Installation Steps](#installation-steps)
2. [API Usage](#api-usage)
   - [List FAQs](#list-faqs)
   - [FAQ Translations](#faq-translations)
3. [Models and Translation Logic](#models-and-translation-logic)
4. [Docker Setup](#docker-setup)
5. [Contribution Guidelines](#contribution-guidelines)
6. [License](#license)

---

## Installation Steps

### Prerequisites
- Python 3.8+
- Docker and Docker Compose

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/KartikMouli/BharatFD_backend.git
cd BharatFD_backend
```

### 2. Set up Virtual Environment (Optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
Make sure `pip` is installed, then install the required packages:
```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes dependencies like:
- `Django`
- `djangorestframework`
- `googletrans`
- `ckeditor`

### 4. Set up the Database
Run the following commands to set up the database:
```bash
cd faq_project
python manage.py migrate
```

### 5. Create a Superuser (for Django Admin)
To interact with the Django Admin, you need to create a superuser:
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
Run the development server:
```bash
python manage.py runserver
```

Now, you can access the API and admin interface on `http://127.0.0.1:8000/`.

---

## API Usage

### List FAQs

You can fetch the list of FAQs with translations using the following endpoint:

**GET** `/api/faqs/`

#### Example Request:
```bash
curl -X GET "http://127.0.0.1:8000/api/faqs/"
```

#### Example Response:
```json
[
  {
    "question": "What is Django?",
    "answer": "Django is a high-level Python web framework.",
    "question_hi": "Django क्या है?",
    "answer_hi": "Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।",
    "question_bn": "ডjango কী?",
    "answer_bn": "ডjango একটি উচ্চ স্তরের Python ওয়েব ফ্রেমওয়ার্ক।"
  },
  ...
]
```

### FAQ Translations

To get a specific translation of an FAQ, use the `lang` query parameter to specify the language.

**GET** `/api/faqs/?lang=hi`

This will return the FAQs in Hindi.

#### Example Request:
```bash
curl -X GET "http://127.0.0.1:8000/api/faqs/?lang=hi"
```

#### Example Response:
```json
[
  {
    "question": "Django क्या है?",
    "answer": "Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।",
    ...
  }
]
```

Supported languages: `en` (English), `hi` (Hindi), `bn` (Bengali).

---

## Models and Translation Logic

The `FAQ` model contains the following fields:
- `question`: The main question in English.
- `answer`: The answer to the question in English.
- `question_hi`: The translated question in Hindi.
- `answer_hi`: The translated answer in Hindi.
- `question_bn`: The translated question in Bengali.
- `answer_bn`: The translated answer in Bengali.

### Translation Logic:
- Translations for Hindi and Bengali are automatically generated when saving a new FAQ or updating an existing one.
- Translations are cached for better performance.
- Google Translate API is used for translations.

---

## Docker Setup

This project is containerized using Docker. Follow the steps below to set up the project with Docker:

### 1. Install Docker and Docker Compose
Ensure Docker and Docker Compose are installed on your system.

### 2. Start the Containers
Run the following command to build and start the containers:
```bash
docker-compose up --build
```

This will set up:
- A PostgreSQL database container
- A Redis caching container
- The Django application container

### 4. Access the Application
Once the containers are up and running, you can access the application at `http://localhost:8000/`.

### 5. Running Migrations and Creating a Superuser
To run migrations or create a superuser, execute the following commands in the Django container:
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

---

## Contribution Guidelines

We welcome contributions to this project! If you'd like to contribute, please follow these guidelines:

1. **Fork the repository** and create your branch (`git checkout -b feature-name`).
2. **Make your changes** in the new branch.
3. **Commit your changes** (`git commit -am 'Add new feature'`).
4. **Push to your fork** (`git push origin feature-name`).
5. **Create a pull request** with a clear description of what your changes do.

### Code Style:
- Follow the existing code style in the repository.
- Use meaningful names for variables, methods, and classes.
- Ensure that all code is well-documented and follows Python's PEP 8 guidelines.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

