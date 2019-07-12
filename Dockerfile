FROM python:3

ADD  viewomdb.py /

#RUN pip install packagename

CMD [ "python", "./viewomdb.py"]
