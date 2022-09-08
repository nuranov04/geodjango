FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
ADD requirements.txt /app/backend/
RUN pip install --upgrade pip

# Setup GDAL
RUN apt-get update

RUN apt-get install -y libgdal-dev g++ --no-install-recommends && \
    pip install whitenoise && \
    apt-get clean -y


RUN pip install -r /app/backend/requirements.txt
RUN pip install psycopg2-binary
ADD docker /app/docker
ADD . /app/backend
EXPOSE 8000
RUN ["chmod", "+x", "/app/docker/backend/wsgi-entrypoint.sh"]