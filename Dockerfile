FROM python:3.8
# automatically install updated version of pip
RUN pip install --upgrade pip
# set virtual enviroment (pipenv)
RUN pip install pipenv
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# set working directory
WORKDIR /code
# copy requirements.txt to working directory
COPY requirements.txt /code/
# install packages
RUN pip install -r requirements.txt
# copy project to working directory
COPY . /code/ 
