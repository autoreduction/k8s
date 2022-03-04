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
RUN python3 -m pip install --user --no-cache-dir gunicorn autoreduce-frontend==22.0.0.dev17

USER root
RUN mkdir -p /staticfiles
RUN mkdir -p /var/www/api/
RUN chown isisautoreduce:isisautoreduce /staticfiles
RUN chown isisautoreduce:isisautoreduce /var/www/api/
USER isisautoreduce
RUN ["autoreduce-webapp-manage", "collectstatic", "--no-input"]
RUN cp -R /staticfiles /var/www/api/

EXPOSE 8000
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "autoreduce_frontend.autoreduce_webapp.wsgi"]
