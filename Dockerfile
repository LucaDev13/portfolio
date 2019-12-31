FROM python:3.7

ENV FLASK_ENV=development
ENV FLASK_APP=portfolio_app.portfolio:start_app

RUN apt-get update

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV FLASK_RUN_PORT=5000
EXPOSE ${FLASK_RUN_PORT}
CMD ["flask", "run", "--host", "0.0.0.0"]