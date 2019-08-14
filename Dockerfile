FROM python:3

ADD  viewomdb.py /

#RUN pip install packagename
RUN pip install sys requests

CMD [ "python", "./viewomdb.py"]
