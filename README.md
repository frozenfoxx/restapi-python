# restapi-python

[![Build Status](https://cloud.drone.io/api/badges/frozenfoxx/restapi-python/status.svg?ref=refs/heads/main)](https://cloud.drone.io/frozenfoxx/restapi-python)

Example REST API in Python.

# Requirements

* [Docker](https://www.docker.io/).

# Build

```
git clone https://github.com/frozenfoxx/restapi-python restapi-python
cd restapi-python
docker build -t frozenfoxx/restapi-python:latest .
```

# Run

```
docker run \
  -it \
  --rm \
  -p 8080:8080 \
  frozenfoxx/restapi-python:latest
```

## Environment Variables

* **HOST**: which IP/FQDN to listen on (default: 0.0.0.0)
* **PORT**: which port to listen on (default: 8080)

# Usage

## Create

* `curl --request POST --url http://[host]:[port]/signatures/[ID]`: create a new signature, ID.

## Read

* `curl --request GET --url http://[host]:[port]/signatures`: retrieve all signatures.
* `curl --request GET --url http://[host]:[port]/signatures/[ID]`: retrieve ID's signature

## Update

* `curl --request PUT --url http://[host]:[port]/signatures/[ID]`: update the time ID has signed.

## Delete

* `curl --request DELETE --url http://[host]:[port]/signatures/[ID]`: delete ID's signature.
