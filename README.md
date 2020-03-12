# avogadro2-docker

## How to build Avogadro2 v1.93.0-1
 * For Fedora Core 32

	$ docker build -f ./Dockerfile.fedora32 -t avogadro2:fedora32 .

 * For CentOS7/SL7

	$ docker build -f ./Dockerfile.el7 -t avogadro2:el7 .


## Running the docker container

	$ docker run --rm -it -e DISPLAY=:0 -v /tmp/.X11-unix:/tmp/.X11-unix avogadro2:el7 


## Status

 * CentOS7 build is successful
 * Generating an RPM for Nanocar plugin --> A dependency issue of python3.6 packages

 * Fedore32 build is unsuccessful

