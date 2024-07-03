# Use the official Python 3.12.3 base image from the Docker Hub
FROM python:3.12.3

# Install required system packages for Tkinter and X11
RUN apt-get update && \
    apt-get install -y python3-tk x11-apps

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the application code to the working directory
COPY . .

# Set environment variable to allow access to host display
ENV DISPLAY=:0

# Specify the command to run the application
CMD ["python", "main.py"]
