# syntax=docker/dockerfile:experimental

ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

WORKDIR /app

RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
    apt-get update \
 && apt-get install taskwarrior

COPY . .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install .

ENTRYPOINT [ "/bin/bash", "-c" ]

CMD [ "/app/test/test.sh" ]
