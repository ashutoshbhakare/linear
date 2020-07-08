FROM python:3.6
RUN mkdir /code

RUN pip install -r req.txt

ADD . /code
WORKDIR /code

ENTRYPOINT ["python3.6","python.py"]
CMD ["1000"]
