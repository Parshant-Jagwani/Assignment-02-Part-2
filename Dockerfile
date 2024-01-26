# Use the official Python image as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install pip
RUN apt-get update && apt-get install -y python3-pip

# Upgrade pip
RUN pip install --upgrade pip setuptools

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
