FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip install -r requirements.txt

WORKDIR /app/Package
RUN pip install apttuskeyvaluestoreprovider-0.1.tar.gz

#RUN pip install dependency-injector-3.14.2.tar.gz
RUN apk del .build-deps gcc musl-dev
WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app/Package/server"
CMD python KeyController.py
