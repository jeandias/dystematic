#!/bin/sh -e
hostname=$(hostname -f)

case "$1" in
    django)
        ./manage.py migrate
        case "$ENVIRONMENT" in
            local)
                ./manage.py runserver 0.0.0.0:8000
                ;;
            *)
                /usr/local/bin/gunicorn \
                    dystematic.wsgi:application \
                    --access-logfile - \
                    --error-logfile - \
                    -n django_site
                ;;
        esac
        ;;
    celery)
        rm -rf celerybeat.pid
        case "${CELERY_QUEUE}" in
            beat)
                celery -A dystematic beat \
                    -l ${CELERY_LOGLEVEL:-info} \
                ;;
            *)
                celery -A dystematic worker \
                    --autoscale=3,6 \
                    -Ofair \
                    -Q ${CELERY_QUEUE:-celery} \
                    -n ${CELERY_QUEUE:-celery}@%h \
                    -l ${CELERY_LOGLEVEL:-info} \
                ;;
        esac
        ;;
    *)
        exec "$@"
        ;;
esac
