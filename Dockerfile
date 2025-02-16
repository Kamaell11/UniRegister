# Description: Dockerfile for Python 3.9 with Tkinter support
FROM python:3.9-slim

# Install Tkinter
RUN apt-get update && \
    apt-get install -y python3-tk && \
    apt-get clean

# Make a directory for our application
WORKDIR /app

# Copy requirements
COPY requirements.txt /app/

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . /app/

# Run the application
CMD ["python", "main.py"]
