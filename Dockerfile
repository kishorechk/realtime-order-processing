# Dockerfile for custom base image
FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y wget tar \
    && pip install --upgrade pip

RUN wget -O flyway.tar.gz https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/7.15.0/flyway-commandline-7.15.0-linux-x64.tar.gz \
    && tar -xzf flyway.tar.gz -C /opt \
    && ln -s /opt/flyway-7.15.0/flyway /usr/local/bin