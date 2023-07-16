# Use the official Python base image
FROM python:3.11.1

# Set the working directory in the container
WORKDIR /FastAPI

# Copy the requirements file
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY ./src .

# Expose the port that the FastAPI application will listen on
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
