FROM python:3-alpine

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY gpt.py .
RUN chmod +x gpt.py

# Set entrypoint
ENTRYPOINT ["./gpt.py"]
