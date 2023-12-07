
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
cd ../E---3.0.03/build
podman build -t e---3.0.03-build .
```

Now build `e---control` image:
```shell
cd ../../E---control
podman build -t e---control .
```

Now run the image to see the results:
```shell
cd ../../ # back to docker-stuff dir
podman run -v "$PWD/MPT0001+1.p":"/artifacts/MPT0001+1.p" -t e---control MPT0001+1.p 10 THM
```


