FROM ubuntu-build

RUN git clone --recurse-submodules https://github.com/TPTPWorld/ServiceTools.git
RUN git clone --recurse-submodules https://github.com/TPTPWorld/TPTP4X.git

# installs after clones (the clones take a while)
RUN apt-get update && apt-get install -y --no-install-recommends libcurl4 libcurl4-gnutls-dev numactl libnuma-dev

# Build tptp stuff. /artifacts is where we put all relevant executables and is the working dir.
# It is created in ubuntu-build
ENV TPTP_HOME /
RUN cd ServiceTools/JJUsers && make SPCForProblem 
RUN cd TPTP4X && make tptp4X
RUN cp ServiceTools/JJUsers/SPCForProblem /artifacts/
RUN cp TPTP4X/tptp4X /artifacts/

# build runsolver
RUN wget --no-check-certificate https://www.cril.univ-artois.fr/~roussel/runsolver/runsolver-3.4.1.tar.bz2
RUN tar -xjf runsolver-3.4.1.tar.bz2 
WORKDIR /runsolver/src
RUN make
RUN cp /runsolver/src/runsolver /artifacts/

# /benchmark is where we put the TPTP problem.
RUN mkdir -p /benchmark

WORKDIR /artifacts

#----Not using benchexec for now, need this (or Sofia's C version) in the future.
# # build benchexec/runexec
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-base \
#     gcc \
#     openssl-dev \
#     bzip2-dev \
#     libffi-dev \
#     zlib-dev \
#     sqlite-dev \
#     xz-dev \
#     tk-dev \
#     db-dev \
#     gdbm-dev \
#     ncurses-dev \
#     readline-dev \
#     wget \
#     python3 \
#     python3-dev
# 
# # Downloading and building Python 3.9
# WORKDIR /tmp
# RUN wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz \
#     && tar -xvf Python-3.9.6.tgz \
#     && cd Python-3.9.6 \
#     && ./configure \
#     && make \
#     && make altinstall
# 
# # Installing pip for Python 3.9
# RUN wget https://bootstrap.pypa.io/get-pip.py \
#     && /usr/local/bin/python3.9 get-pip.py
# 
# # Installing benchexec with pip
# RUN /usr/local/bin/python3.9 -m pip install benchexec
# 
# # Creating a directory for benchexec
# RUN mkdir /home/benchexec

