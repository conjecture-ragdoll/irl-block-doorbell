FROM python:3.12.2

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set the working directory in the container
WORKDIR /app

# Install virtual environment tool
RUN pip3 install virtualenv

# Create and activate a virtual environment
RUN virtualenv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# Copy the project code into the container
COPY . /app/

EXPOSE 8000

# Command to run the application
# CMD ["python", "app.py"]
