FROM python:3

ADD  viewomdb.py /

#RUN pip install packagenameifreq

CMD [ "python", "./viewomdb.py"]
