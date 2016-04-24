FROM python:3

MAINTAINER Tully Rankin

COPY . /src
WORKDIR /src

RUN pip install -r /src/requirements.txt
CMD ["python", "manage.py", "serve"]
