# Ntp-Docker


Este repositorio contine 2 Dockerfiles uno correspondiente al servidor y el otro al cliente, del protcolo NTP(Network Time Protocol).

Los cuales estan creados a base de 2 proyectos existentes en github.

Servidor: https://github.com/limifly/ntpserver ; Version: 1.0

Cliente: https://github.com/KikyTokamuro/tinyntp ; Version: 1.0

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

