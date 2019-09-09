FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_graphql
WORKDIR /django_graphql
COPY requirenments/base.txt /django_graphql
COPY requirenments/dev.txt /django_graphql
RUN pip install -r dev.txt
COPY . /django_graphql