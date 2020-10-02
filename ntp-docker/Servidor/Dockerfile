FROM ubuntu

MAINTAINER Nicolas Frias "nicolas.frias@mail.udp.cl"

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /ntp-server

RUN apt-get -yqq update \
&& apt-get -y upgrade \
&& apt-get install -yqq build-essential git \
&& apt-get install -yqq python2 \
&& git clone https://github.com/limifly/ntpserver.git
WORKDIR /ntp-server/ntpserver
EXPOSE 123
RUN echo  "export PATH=/usr/lib/python2:$PATH" >> ~/.bashrc

ENTRYPOINT ["python2","ntpserver.py"]
