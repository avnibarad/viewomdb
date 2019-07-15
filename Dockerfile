FROM python:3

ADD  viewomdb.py /

#RUN pip install packagename
RUN pip install omdb

CMD [ "python", "./viewomdb.py"]
