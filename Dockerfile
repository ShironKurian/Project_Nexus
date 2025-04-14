# Use a lightweight Python base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Specify the command to run your application
CMD ["python", "app.py"]

MAINTAINER shironkurian@gmail.com

ENTRYPOINT ["python", "app.py"]