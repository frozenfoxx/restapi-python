#!/usr/bin/env ash

pip3 install .

uvicorn app.main:app --host ${HOST} --port ${PORT} $@