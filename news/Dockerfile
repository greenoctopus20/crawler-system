# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the server script and the articles folder into the container
COPY server.py .
COPY requirements.txt .
COPY articles/ ./articles

# Expose port 9000
EXPOSE 9000

# Install any dependencies (if required)
RUN pip install -r requirements.txt

# Command to run the server
CMD ["python","-u" , "server.py"]

