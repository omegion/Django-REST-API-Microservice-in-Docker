FROM python:3.6

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements/production.txt

COPY ./docker/production/web/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]
