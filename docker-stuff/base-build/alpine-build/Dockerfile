FROM alpine:latest

# Install build dependencies
RUN apk add --update build-base bash git

# PicoSAT fix (see https://stackoverflow.com/questions/52894632/cannot-install-pycosat-on-alpine-during-dockerizing)
# In musl (the libc library implementation used in Alpine) the unistd.h header is located at the system headers root folder (/usr/include) 
# and not under /usr/include/sys as in glibc, and therefore compilation may fail with fatal error: "sys/unistd.h: No such file or directory".
# As a workaround, we create our own header under sys/unistd.h which will simply includes the native unistd.h
RUN  if ! test -e /usr/include/sys/unistd.h; then echo "#include <unistd.h>" > /usr/include/sys/unistd.h; fi
#RUN echo "#include <unistd.h>" > /usr/include/sys/unistd.h


# Configure GIT to clone repos
RUN export GIT_SSL_NO_VERIFY=1 && \
    git config --global http.sslverify false

# Create "/artifacts" directory for build artifacts
RUN mkdir /artifacts/

ENTRYPOINT ["/bin/bash"]
