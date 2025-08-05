# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies directly
RUN pip install --no-cache-dir fastapi uvicorn boto3

# Copy all project files into container
COPY . .

# Expose port (FastAPI default)
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
