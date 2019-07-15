FROM python:3

ADD  viewomdb.py /

#RUN pip install packagename
pip install omdb

CMD [ "python", "./viewomdb.py"]
