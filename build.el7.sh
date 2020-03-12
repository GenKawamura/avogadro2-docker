#!/bin/bash

usage="$0 [build|run]"

[ $# -eq 0 ] && echo "$usage" && exit 0

case $1 in
    build)
	docker build -f Dockerfile.el7 -t avogadro2:el7 .
	;;
    run)
	docker run --rm -it -e DISPLAY=:0 -v /tmp/.X11-unix:/tmp/.X11-unix avogadro2:el7
	;;
    *)
	echo "No such option [$1]"
	;;
esac

