# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the entire application folder to the working directory
COPY . /app/

# Expose the port the application will run on
EXPOSE 8000

# Command to run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:server"]
