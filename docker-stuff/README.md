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

First clone this repo and build `alpine-build` image:
```shell
git clone https://github.com/StarExecMiami/starexec-kubernetes.git
cd starexec-kubernetes/docker-stuff/base-build/alpine-build
podman build -t alpine-build .
podman image ls   # to see what was built
```

Now build `tptp-world-build` image:
```shell
cd ../tptp-world-build
podman build -t tptp-world-build .
```

Now build `e---3.0.03-build` image:
```shell
cd ../provers/E---3.0.03/build/
podman build -t e---3.0.03-build .
```

Now build `e---control` image:
```shell
cd ../../E---runsolver
podman build -t e---runsolver .
```

Now run the image to see the results:
```shell
cd ../../ # back to docker-stuff dir
podman run -v "$PWD/MPT0001+1.p":"/artifacts/MPT0001+1.p" -t e---control MPT0001+1.p 10 THM
```

## To run using the E---runsolver.py script

python3 E---runsolver.py PUZ001+1.p 

## To put it in dockerhub

podman login docker.io
podman tag e---runsolver docker.io/geoffgeoffgeoff3/starexec-provers-e-runsolver:latest
podman push docker.io/geoffgeoffgeoff3/starexec-provers-e-runsolver:latest

## To pull it from dockerhub

podman pull geoffgeoffgeoff3/starexec-provers-e-runsolver

## To run it 

You need the E---runsolver.py script and a problem e.g., PUZ001+1.p (both in GitHub)
python3 E---runsolver.py --image-name docker.io/geoffgeoffgeoff3/starexec-provers-e-runsolver PUZ001+1.p


