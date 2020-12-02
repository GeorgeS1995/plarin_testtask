FROM python:3.9.0-slim-buster
ENV CONTRIB_FASTAPI_APP=main.app
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/
EXPOSE 80