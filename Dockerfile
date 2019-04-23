FROM python:3.6

#RUN apt-get update &&\
#    apt-get -y --no-install-recommends install \
#    ca-certificates curl && \
#    useradd -ms /bin/bash bulkcat

ADD simple_back /app/simple_back
ADD setup.py /app/

WORKDIR /app

RUN pip install --upgrade pip && pip install .

#USER bulkcat

CMD ["gunicorn", "simple_back.gunicorn:app", "-c", "simple_back/gunicorn.conf.py", "--access-logfile", "-"]

HEALTHCHECK CMD curl -f localhost:8000/hc || exit 1
