#!/usr/bin/env bash

pip3 install .

uvicorn app.main:app --host ${HOST} --port ${PORT} $@