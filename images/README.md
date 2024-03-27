## GENERAL INFO ##
The container images in the folder "provers" depend on (some of) the images in the folder 
"base-build".

We recommend using Podman (which is intended to work as a drop-in replacement for Docker).
See Podman installation instructions: https://podman.io/docs/installation

## How to do podman/docker actions

Building a container image with Podman/Docker:
>> podman/docker build -t <TAG_NAME> <PATH_TO_DIRECTORY_WHERE_DOCKERFILE_LIES>

Running a container (from an image) with Podman/Docker (entrypoint):
>> podman/docker run --rm [--entrypoint <ENTRYPOINT_FILE>] <TAG_NAME> <ARGS>

Running a container with Podman/Docker (interactive shell):
>> podman/docker run --rm -it <TAG_NAME>

Cleanup everything (Podman):
podman system prune --all --force && podman rmi --all

Forced cleanup (Podman):
podman rmi --all --force

Cleanup everything (Docker):
docker system prune --all --force &&  docker rmi $(docker images -a -q)


## To build and run a TPTP docker image for E (example)

First clone this repo and build `ubuntu-build` image:
```shell
git clone https://github.com/StarExecMiami/starexec-kubernetes.git
cd starexec-kubernetes/docker-stuff/base-build/ubuntu-build
podman build -t ubuntu-build .
podman image ls   # to see what was built
```

Now build `tptp-world-build` image:
```shell
cd tptp-world-build
podman build -t tptp-world-build .
```

Now build `eprover-build` image. Note that the version number is not in the tag, so the next
step to build the eprover:version-runsolver image will always use the eprover-build:latest, 
which might be a new version of E.
```shell
cd provers/eprover/E---3.0.03/build/
podman build -t eprover-build .
```

Now build `eprover:version-runsolver` image:
```shell
cd ../../E---runsolver
podman build -t eprover:3.0.03-runsolver .
```

## To run using the runsystem.py script

```shell
runsystem.py eprover:3.0.03-runsolver -P ../TPTP-problems/PUZ001+1.p -W 60 -I THM
```

## To put it in dockerhub

podman login docker.io (tptpstarexec, German greeting with money-in-middle and zeros-at-the-end)
podman tag eprover:3.0.03-runsolver docker.io/tptpstarexec/eprover:3.0.03-runsolver-your_architecture (e.g., arm64, amd64)
podman push docker.io/tptpstarexec/eprover:3.0.03-runsolver-your_architecture

## To pull it from dockerhub

podman pull tptpstarexec/e-runsolver:your_architecture

