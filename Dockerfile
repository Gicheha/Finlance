FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.pip /config/
RUN mkdir /src;
WORKDIR /src
COPY . /src/
RUN pip install -r /config/requirements.pip
RUN pip install mysqlclient
