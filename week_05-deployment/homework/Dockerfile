FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["q6_service.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind" , "0.0.0.0:9696", "q6_service:app"]