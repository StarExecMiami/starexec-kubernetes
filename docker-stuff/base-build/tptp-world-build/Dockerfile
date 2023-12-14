FROM alpine-build
RUN apk update && apk add --no-cache tcsh git 
RUN git clone --recurse-submodules https://github.com/TPTPWorld/ServiceTools.git
RUN git clone --recurse-submodules https://github.com/TPTPWorld/TPTP4X.git

# more installs after clones (the clones take a while)
RUN apk update && apk add --no-cache curl build-base gcc curl-dev curl libcurl

# build tptp stuff
ENV TPTP_HOME /
RUN cd ServiceTools/JJUsers && make SPCForProblem 
RUN cd TPTP4X && make tptp4X
RUN cp ServiceTools/JJUsers/SPCForProblem /artifacts/
RUN cp TPTP4X/tptp4X /artifacts/


# build runsolver
RUN apk add --upgrade git g++ make numactl numactl-dev
RUN git clone https://github.com/utpalbora/runsolver.git
WORKDIR /runsolver/src
RUN make
RUN cp /runsolver/src/runsolver /artifacts/

# build benchexec/runexec
RUN apk update && apk add --no-cache \
    build-base \
    gcc \
    openssl-dev \
    bzip2-dev \
    libffi-dev \
    zlib-dev \
    sqlite-dev \
    xz-dev \
    tk-dev \
    db-dev \
    gdbm-dev \
    ncurses-dev \
    readline-dev \
    wget \
    python3 \
    python3-dev

# Downloading and building Python 3.9
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz \
    && tar -xvf Python-3.9.6.tgz \
    && cd Python-3.9.6 \
    && ./configure \
    && make \
    && make altinstall

# Installing pip for Python 3.9
RUN wget https://bootstrap.pypa.io/get-pip.py \
    && /usr/local/bin/python3.9 get-pip.py

# Installing benchexec with pip
RUN /usr/local/bin/python3.9 -m pip install benchexec

# Creating a directory for benchexec
RUN mkdir /home/benchexec



# Convention:
# /artifacts/ is where we will put all relevant executables and will the working dir.
# /benchmark/ is where we will put the TPTP problem.
RUN mkdir -p /artifacts
RUN mkdir -p /benchmark

WORKDIR /artifacts


