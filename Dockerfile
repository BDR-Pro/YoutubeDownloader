# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . . 

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn


# Expose the port that the app will run on
EXPOSE 8000



# Run command to start the application
CMD python YoutubeDownloader/manage.py runserver 0.0.0.0:8000

