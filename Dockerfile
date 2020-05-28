FROM python:3.7.7-buster
COPY ./src /src
ADD requirements.txt /requirements.txt
ADD run_worker.sh /run_worker.sh
ENV PYTHONPATH "/"
RUN pip3 install -r requirements.txt
RUN ["chmod", "+x", "/run_worker.sh"]
CMD ./run_worker.sh
