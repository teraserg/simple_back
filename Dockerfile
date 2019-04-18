FROM python:3.6

ADD mtail_progs /etc/mtail_progs
RUN apt-get update && apt-get install golang-go mtail vim -y && \
    mkdir -p /var/log/gunicorn && \
    go version

# Configure Go
ENV GOROOT /usr/lib/go
ENV GOPATH /go
ENV PATH /go/bin:$PATH

#RUN apt-get update &&\
#    apt-get -y --no-install-recommends install \
#    ca-certificates curl && \
#    useradd -ms /bin/bash simpleback

ADD simple_back /app/simple_back
ADD setup.py run.sh /app/

WORKDIR /app

RUN pip install --upgrade pip && pip install . && chmod +x run.sh

#USER simpleback

CMD ./run.sh

HEALTHCHECK CMD curl -f localhost:8000/hc || exit 1
