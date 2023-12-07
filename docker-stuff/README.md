git clone https://github.com/StarExecMiami/starexec-kubernetes.git
cd starexec-kubernetes/docker-stuff/
cd base-build
cd alpine-build
podman build -t alpine-build .
podman image ls   # to see what was built
cd ../../provers/E---3.0.03/build
podman build -t e---3.0.03-build .
cd ../..
mkdir E---control
cd E---control
podman build -t e---control .

