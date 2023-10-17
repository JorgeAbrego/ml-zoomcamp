## How to use pipenv

Install pipenv running the following command:

> pipenv install scikit-learn=1.3.1

More modules can be added running:

> pipenv install flask gunicorn waitress

If you want to run a python file inside venv, just run:

> pipenv run python q3.py

Running a service over gunicorn server on Linux using venv:

> pipenv run gunicorn --bind 0.0.0.0:9696  q4_service:app

Running a service over waitress server on Windows using venv:

> pipenv run waitress-serve --listen=0.0.0.0:9696  q4_service:app

## Using Docker

Bulding image:

> docker build -t bank-credit-scoring:v1 .

Run container:

> docker run -it --name BankCreditScoring -p 9696:9696 bank-credit-scoring:v1