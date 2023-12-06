FROM adoptopenjdk/openjdk11:alpine

# Install dependencies
RUN apk add --update build-base curl bash dpkg shadow git

# Configure GIT to clone repos
RUN export GIT_SSL_NO_VERIFY=1 && \
    git config --global http.sslverify false

# PicoSAT fix (see https://stackoverflow.com/questions/52894632/cannot-install-pycosat-on-alpine-during-dockerizing)
# In musl (the libc library implementation used in Alpine) the unistd.h header is located at the system headers root folder (/usr/include) 
# and not under /usr/include/sys as in glibc, and therefore compilation may fail with fatal error: "sys/unistd.h: No such file or directory".
# As a workaround, we create our own header under sys/unistd.h which will simply includes the native unistd.h
RUN  if ! test -e /usr/include/sys/unistd.h; then echo "#include <unistd.h>" > /usr/include/sys/unistd.h; fi


######### Install SBT ############
ARG SBT_VERSION=1.6.2
# prevent this error: java.lang.IllegalStateException: cannot run sbt from root directory without -Dsbt.rootdir=true; see sbt/sbt#1458
WORKDIR /app
# Download and install SBT debian package
RUN curl -L -o sbt-$SBT_VERSION.deb https://repo.scala-sbt.org/scalasbt/debian/sbt-$SBT_VERSION.deb
RUN dpkg --configure -a && \
    dpkg --ignore-depends=bash -i sbt-$SBT_VERSION.deb
# Cleanup
RUN  rm sbt-$SBT_VERSION.deb
# Init SBT
RUN sbt sbtVersion

# Create "/artifacts" directory for build artifacts
RUN mkdir /artifacts/

ENTRYPOINT ["/bin/bash"]
