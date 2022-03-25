# Don't use alpine based images: Python was designed for glibc and is very slow in them.
# Always use the -slim images if you can: they are the best compromise between performance and image size.
FROM python:3.8.12-slim

# Set production env to ensure DEBUG+False for Django
# This sets STATIC_ROOT to /staticfiles
ENV AUTOREDUCTION_PRODUCTION 1

# This is to print directly to stdout instead of buffering output
ENV PYTHONUNBUFFERED 1

RUN export DEBIAN_FRONTEND=noninteractive && apt-get update &&\
    apt-get install -y wget gnupg git software-properties-common python3-dev default-libmysqlclient-dev build-essential

RUN pip install dumb-init

# Create non-root user and configure it for the project to run correctly with it.
RUN useradd -m --no-log-init -s /bin/bash -u 880844730 isisautoreduce
USER isisautoreduce
WORKDIR /home/isisautoreduce

# .local/bin is where local pip packages put their executables
ENV PATH=/home/isisautoreduce/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Note: mysqlclient is required when connecting to the production DB
RUN python3 -m pip install --user --no-cache-dir mysqlclient debugpy

ADD ./setup.py /autoreduce-rest-api/setup.py

# add --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple for packages in test.pypi.org
RUN python3 -m pip install --no-cache-dir gunicorn autoreduce-rest-api==22.0.0.dev14

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "autoreduce_rest_api.autoreduce_django.wsgi"]
