ARG PYTHON_VERSION=3.8
ARG DEBIAN_VERSION=buster

##############################################################################
# BE cache
FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION} as python-cache
# FROM be-build-base as python-cache
ARG SSHKEY
ARG KNOWN_HOSTS

COPY requirements.txt /tmp/requirements.txt

RUN pip wheel --wheel-dir=/root/wheels -r /tmp/requirements.txt

##############################################################################
# Application image
FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION}

ENV PYTHONUNBUFFERED 1
ENV APP_FOLDER=/var/www/app

WORKDIR ${APP_FOLDER}

RUN : "---------- install container extras ----------" \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        vim \
        jq \
        curl \
        netcat \
        procps \
        openssl \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY --from=python-cache /root/wheels /root/wheels
RUN WHEELS=$(cd /root/wheels; ls -1 *.whl | awk -F - '{ gsub("_", "-", $1); print $1 }' | uniq) \
    && pip install --no-index --find-links=/root/wheels $WHEELS

COPY rootfs /
COPY . ${APP_FOLDER}
WORKDIR ${APP_FOLDER}

RUN ./manage.py collectstatic --noinput -i img_src

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

HEALTHCHECK \
    --start-period=15s \
    --timeout=14s \
    --retries=1 \
    --interval=20s \
    CMD /healthcheck.sh