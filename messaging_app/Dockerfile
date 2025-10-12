docker run -p 8000:8000 messaging_app_image

# Use official Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose Django's default port
EXPOSE 8000

# Run the Django app (adjust if using manage.py or gunicorn)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
