# Base image
FROM python:3.7

# Information
LABEL maintainer="FrozenFOXX <frozenfoxx@churchoffoxx.net>"

# Variables
ENV APPDIR="/app" \
  HOST="0.0.0.0" \
  PORT="8080"

WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

# Expose listen port
EXPOSE 8080

# Launch
ENTRYPOINT [ "./scripts/entrypoint.sh" ]
