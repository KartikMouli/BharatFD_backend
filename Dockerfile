# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 (Django's default)
EXPOSE 8000

# Set environment variable to avoid Python writing pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Set environment variable to ensure Django uses the correct settings module
ENV DJANGO_SETTINGS_MODULE=faq_project.settings


# Run Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
