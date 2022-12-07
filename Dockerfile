FROM python:3.12.0a2-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBUFFERED 1

WORKDIR /projects/blogsite

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . . 
