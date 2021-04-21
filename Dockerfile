FROM ubuntu:20.04

ENV USER SOURAV

RUN mkdir /code

WORKDIR /code

RUN apt-get update -y
RUN apt-get install -y python3.4 python3-pip
RUN pip3 install Django==3.2
#RUN pip3 install mysqlclient
#RUN apt-get install -y Django==2.2
#RUN sudo pip3 install -r requirements.txt
#RUN pip3 install --upgrade pip
#RUN pip3 install django

COPY . /code/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]