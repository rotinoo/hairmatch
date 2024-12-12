# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from the requirements.txt file
RUN pip install -r requirements.txt

EXPOSE 8080

# Command to run the Streamlit app
CMD ["streamlit", "run", "Home.py", "--server.port", "8080"]