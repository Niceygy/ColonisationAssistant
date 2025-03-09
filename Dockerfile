FROM python:slim-bullseye

# Copy application code
COPY . /home/

# Set workdir
WORKDIR /home

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 5005

# Labels
LABEL org.opencontainers.image.description="Colonisation assiatant"
LABEL org.opencontainers.image.authors="Niceygy (Ava Whale)"

# Start Gunicorn
CMD gunicorn -c gunicorn_config.py app:app