FROM python:3

ADD  viewomdb.py /

#RUN pip install packagename
RUN pip install requests

CMD [ "python", "./viewomdb.py"]
