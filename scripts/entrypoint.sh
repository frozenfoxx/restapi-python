#!/usr/bin/env bash

pip3 install .

uvicorn restapi.main:app --host ${HOST} --port ${PORT} $@