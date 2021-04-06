ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

WORKDIR /app

RUN apt-get update \
 && apt-get install taskwarrior \
 && yes yes | task version

COPY . .

RUN pip install .

RUN /app/test/test.sh
