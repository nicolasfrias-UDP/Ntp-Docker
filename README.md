# Ntp-Docker


Este repositorio contine 2 Dockerfiles uno correspondiente al servidor y el otro al cliente, del protcolo NTP(Network Time Protocol).

Los cuales estan creados a base de 2 proyectos existentes en github.

Servidor: https://github.com/limifly/ntpserver ; Version: 1.0

Cliente: https://github.com/KikyTokamuro/tinyntp ; Version: 1.0

Dentro del directorio ntp-docker, se encontrara 2 carpetas una correspondiente al cliente y otra al servidor con sus respectivos dockerfiles y codigos fuente.

### Instalación
Necesario instalar docker, para poder contruir e iniciar las imagenes.

https://docs.docker.com/engine/install/

### Uso

Para construir la imagen ocupamos:
```bash
$ sudo docker build --no-cache -t repository_name:tag_name .
```
Para iniciar:
```bash
$ docker run -ti iamge_id bash 
```
### Polymorph
Video que muestra el proceso de intercepcion y modificacion de paquetes NTP
[![Interceptacion de Paquetes NTP](https://img.gifyoutube.com/vi/T43WTYmAhE4/0.gif)](https://www.youtube.com/watch?v=T43WTYmAhE4)
### test
