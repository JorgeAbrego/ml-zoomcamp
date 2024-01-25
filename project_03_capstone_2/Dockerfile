FROM python:3.10.13-slim-bullseye

WORKDIR /app

RUN pip install --no-cache-dir nltk==3.8.1 scikit-learn==1.3.1 gunicorn==21.2.0 flask==3.0.0

COPY ["predictAPI.py", "labelEncoder.pkl", "tfidfVectorizer.pkl", "randomForestmodelcompressed.pkl", "", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predictAPI:app"]