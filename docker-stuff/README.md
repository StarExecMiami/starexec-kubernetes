######## IMPORTANT ##########
The container images in the folder "provers" depend on (some of) the images in the folder "base-build".
Look at the README file in the corresponding prover's folder for information about image dependencies that need to be built first (and which tags to use).

####### GENERAL INFO #######
We recommend using Podman (which is intended to work as a drop-in replacement for Docker).
See Podman installation instructions: https://podman.io/docs/installation


Building a container image with Podman/Docker:
>> podman/docker build -t <TAG_NAME> <PATH_TO_DIRECTORY_WHERE_DOCKERFILE_LIES>

Running a container (from an image) with Podman/Docker (entrypoint):
>> podman/docker run --rm [--entrypoint <ENTRYPOINT_FILE>] <TAG_NAME> <ARGS>

Running a container with Podman/Docker (interactive shell):
>> podman/docker run --rm -it <TAG_NAME>



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
cd ../tptp-world-build
podman build -t tptp-world-build .
```

Now build `eprover-build` image. Note that the version number is not in the tag, so the next
step to build the eprover:version-runsolver image will always use the eprover-build:latest, 
which might be a new version of E.
```shell
cd ../../provers/eprover/E---3.0.03/build/
podman build -t eprover-build .
```

Now build `eprover:version-runsolver` image:
```shell
cd ../../E---runsolver
podman build -t eprover:3.0.03-runsolver .
```

Now you cannot run the image to see the results:
(Goto next instruction and the python script gives an example if you want 
to see how to actually invoke podman)
```shell
cd ../../../ # back to docker-stuff dir
podman run -v "$PWD/MPT0001+1.p":"/artifacts/MPT0001+1.p" -t e---runsolver MPT0001+1.p 10 THM
```

## To run using the E---runsolver.py script

E---runsolver.py PUZ001+1.p 

## To put it in dockerhub

podman login docker.io (tptpstarexec, German greeting with money-in-middle and zeros-at-the-end)
podman tag eprover:3.0.03-runsolver docker.io/tptpstarexec/eprover:3.0.03-runsolver-your_architecture (e.g., arm64, amd64)
podman push docker.io/tptpstarexec/eprover:3.0.03-runsolver-your_architecture

## To pull it from dockerhub

podman pull tptpstarexec/e-runsolver:your_architecture

## To run it 

You need the E---runsolver.py script and a problem e.g., PUZ001+1.p (both in GitHub)
cd provers/E---runsolver
python3 E---runsolver.py --image-name docker.io/tptpstarexec/e-runsolver:your_architecture PUZ001+1.p


