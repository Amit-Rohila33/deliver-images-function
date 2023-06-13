# Using the official Python image as the base image
FROM python:3.9

# Setting the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY deliver_images.py .

# Installing the required dependencies
RUN pip install aiohttp

# Specifying the command to run the script
CMD ["python", "deliver_images.py"]



# deliverimages:latest
# This is the name of the image if you want to pull and create the corresponding container to it



# Also sir, If you want me to share a .tar file with you, just let me know