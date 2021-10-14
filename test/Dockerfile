# syntax=docker/dockerfile:experimental

FROM python:3

WORKDIR /app

RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
    apt-get update \
 && apt-get install taskwarrior

COPY . .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install .

ENTRYPOINT [ "/bin/bash", "-c" ]

CMD [ "/app/test/test.sh" ]
