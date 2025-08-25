# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy code
COPY server.py .
COPY requirements.txt .

# Install dependencies (none in this case, but good habit)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Start the chat server
CMD ["python", "server.py"]
