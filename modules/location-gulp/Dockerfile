FROM python:3.7-alpine

WORKDIR .

COPY ./modules/location-gulp/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY ./modules/location-gulp/ .
CMD ["python", "main.py"]