# avogadro2-docker

Avogadro2 is a molecure editor and visualization application. The latest version did not run in CentOS7/RHEL7 distribution. This container and patch can generate its workable RPMs.


## How to build Avogadro2 v1.93.0-1 (one can use also ./build.el7.sh)
 * For Fedora Core 32

	$ docker build -f ./Dockerfile.fedora32 -t avogadro2:fedora32 .

 * For CentOS7/SL7

	$ docker build -f ./Dockerfile.el7 -t avogadro2:el7 .


## Running the docker container (one can use also ./build.el7.sh)

	$ docker run --rm -it -e DISPLAY=:0 -v /tmp/.X11-unix:/tmp/.X11-unix avogadro2:el7 


## Status

 * CentOS7 build is successful
 * Generating an RPM for Nanocar plugin --> A dependency issue of python3.6 packages

 * Fedore32 build is unsuccessful

