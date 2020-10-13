FROM ubuntu

MAINTAINER Nicolas Frias "nicolas.frias@mail.udp.cl"

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /ntp-client

RUN apt-get -yqq update \
&& apt-get -y upgrade \
&& apt-get install -yqq build-essential git \
&& git clone https://github.com/nicolasfrias-UDP/Ntp-Docker.git
RUN echo "export PATH=/usr/bin/gcc:$PATH">> ./bashrc
EXPOSE 123
WORKDIR /ntp-client/Ntp-Docker/ntp-docker/Cliente/
RUN gcc tinyntp.c -o tinyntp
ENTRYPOINT  ./tinyntp -h 172.17.0.2 -p 123
