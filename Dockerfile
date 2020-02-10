FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.pip /config/
RUN mkdir /src;
WORKDIR /src
COPY . /src/
RUN pip install -r /config/requirements.pip
CMD apt upgrade
CMD apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
CMD apt install net-tools
