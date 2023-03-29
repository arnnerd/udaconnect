FROM python:3.7-alpine

WORKDIR .

COPY ./modules/location-service/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY ./modules/location-service/ .
CMD ["python", "consumer.py"]