# Use lite python image
FROM python:3.10-slim

# Set up working dir
WORKDIR /app

# Create modules
RUN mkdir -p code

# Copy files
COPY core/logo.py ./core/
COPY core/main.py ./core/
COPY core/probe_request.py ./core/
COPY requirements.txt .
COPY mc_checker.py .
COPY README.md .
COPY LICENSE .

# Run pip3
RUN pip install --no-cache-dir -r requirements.txt

# Launch app
ENTRYPOINT ["python", "mc_checker.py"]