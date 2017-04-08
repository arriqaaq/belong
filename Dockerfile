FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
EXPOSE 8000 8001 8003

ADD . /code/

ENTRYPOINT ["./run.sh"]