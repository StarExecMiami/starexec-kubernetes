FROM eprover-build AS builder

# Switching to Alpine base image
FROM alpine:latest

COPY --from=builder /artifacts/eprover /usr/bin/
COPY --from=builder /artifacts/eprover-ho /usr/bin/

# Installing dependencies needed for building Python 3.9
# Alpine uses 'apk' for package management
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
WORKDIR /home/benchexec

# Setting the entrypoint (optional)
# If you want to run a specific command when the container starts, you can set it here.
# For example, if you want to run the E Prover:
ENTRYPOINT ["runexec"]
