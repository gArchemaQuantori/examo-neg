FROM python:3.7

EXPOSE 8080

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload", "True"]