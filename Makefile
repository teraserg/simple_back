NAME=simple-back
COMMIT=$(shell git rev-parse --short HEAD)

venv:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install --upgrade pip


install: venv
	. venv/bin/activate; \
	pip install -e .


run:
	. venv/bin/activate; \
	python3 simple_back/main.py


run-gu:
	. venv/bin/activate; \
	gunicorn -c simple_back/gunicorn.conf.py --bind localhost:8000 --workers 1 simple_back.gunicorn:app


build-docker:
	docker build -t $(NAME) .
	docker tag $(NAME) $(NAME):$(COMMIT)
