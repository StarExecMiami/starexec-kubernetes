#!/bin/bash

# docker run -v (pwd):(pwd) -w (pwd) eprover MPT0001+1.p --cpu-limit=3 --auto
# docker run -v (pwd):(pwd) -w (pwd) --rm -t runsolver --timestamp -C 20 -W 180 -R 8192 -V 102400 eprover MPT0001+1.p --training-examples=3 --auto


# podman run \
#     --security-opt unmask=/proc/* --security-opt unmask=/sys/fs/cgroup --security-opt seccomp=unconfined \
#     -v $(pwd):$(pwd) -w $(pwd) --rm -t bencheprover --read-only-dir / --overlay-dir /home/benchexec --timelimit=3 -- ls -l /usr/bin;cat output.log

# podman run \
#     --security-opt unmask=/proc/* --security-opt unmask=/sys/fs/cgroup --security-opt seccomp=unconfined \
#     -v $(pwd):$(pwd) -w $(pwd) --entrypoint=bash -it --rm -t bencheprover

podman run \
    --security-opt unmask=/proc/* --security-opt unmask=/sys/fs/cgroup --security-opt seccomp=unconfined \
    -v $(pwd):$(pwd) -w $(pwd) --rm -t bencheprover --read-only-dir / --overlay-dir /home/benchexec --timelimit=3 /usr/bin/eprover MPT0001+1.p
