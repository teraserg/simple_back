#!/usr/bin/env bash

mtail -progs /etc/mtail_progs -logs /var/log/gunicorn/log.log &

cd /app && gunicorn simple_back.gunicorn:app -c simple_back/gunicorn.conf.py --access-logfile - --log-file /var/log/gunicorn/log.log --capture-output
