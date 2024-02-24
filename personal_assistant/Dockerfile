FROM python:3.12.2-alpine

RUN apk update && apk add bash

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./start.sh $APP_HOME/

COPY .. .

RUN chmod +x ./start.sh
RUN ls -la
EXPOSE 8000

# Use the script as the entry point
ENTRYPOINT ["/bin/bash", "start.sh"]
