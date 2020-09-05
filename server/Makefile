.PHONY: start

PYTHON3 ?= python3
ENV ?= . ../env/bin/activate; \
    PYTHONPATH=$(shell realpath ..)

start:
	$(ENV) FLASK_APP=run.py FLASK_ENV=production flask run --port=5000 --host=0.0.0.0
