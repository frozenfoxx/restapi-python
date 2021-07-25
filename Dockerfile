# Base image
FROM python:3-alpine

# Information
LABEL maintainer="FrozenFOXX <frozenfoxx@churchoffoxx.net>"

# Variables
ENV APPDIR="/app" \
  APP_DEPS="build-base openssl-dev python3-dev" \
  HOST="0.0.0.0" \
  PORT="8080"

WORKDIR /app

# Install package dependencies
RUN apk -U add ${APP_DEPS}

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

# Expose listen port
EXPOSE 8080

# Launch
ENTRYPOINT [ "./scripts/entrypoint.sh" ]
