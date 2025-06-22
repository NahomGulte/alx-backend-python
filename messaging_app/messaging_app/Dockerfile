FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy source code
COPY . /app/

# Expose Django port
EXPOSE -p 8000

# Start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

