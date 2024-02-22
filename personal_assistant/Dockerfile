FROM python:3.12.2-alpine

RUN apk update && apk add bash

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

RUN chmod +x ./start.sh

EXPOSE 8000

# Use the script as the entry point
ENTRYPOINT ["./start.sh"]
