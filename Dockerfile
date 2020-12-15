FROM python:3

WORKDIR /app

ENV FLASK_APP=app.py

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app.py .
COPY ./templates/ ./templates/
COPY ./model.pkl .
COPY ./documents.pkl .

RUN ls -lrt

EXPOSE 5000
EXPOSE 8010

CMD ["python", "app.py"]