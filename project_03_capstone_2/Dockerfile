FROM  public.ecr.aws/lambda/python:3.10

RUN pip install --no-cache-dir nltk==3.8.1 scikit-learn==1.3.1 

COPY labelEncoder.pkl .
COPY tfidfVectorizer.pkl .
COPY randomForestmodelcompressed.pkl .
COPY lambda_fnc.py .

CMD [ "lambda_fnc.lambda_handler" ]