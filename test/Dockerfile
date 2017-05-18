FROM alpine

RUN apk add --no-cache task python3 \
 && yes yes|task version

COPY test.sh /test.sh

CMD ["/test.sh"]
