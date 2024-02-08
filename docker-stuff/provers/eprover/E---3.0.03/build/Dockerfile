FROM alpine-build

# Clones repository
ARG E_VERSION=E-3.0.03
RUN git clone --depth 1 --branch $E_VERSION https://github.com/eprover/eprover.git

# Set working directory to cloned sources directory
WORKDIR /eprover

# Builds first-order executable
RUN ./configure --bindir=/artifacts && \
    make && \
    make install
# RUN cp PROVER/eprover /artifacts/eprover

# Builds higher-order executable
RUN ./configure --enable-ho && \
    make rebuild
RUN cp PROVER/eprover-ho /artifacts/eprover-ho

# Smoke tests
RUN echo "############ Smoke tests ############" && \
    /artifacts/eprover --auto EXAMPLE_PROBLEMS/SMOKETEST/LUSK3.p | grep "SZS status Theorem" && \
    /artifacts/eprover-ho --auto EXAMPLE_PROBLEMS/SMOKETEST/LUSK3.p  | grep "SZS status Theorem"

RUN echo "### Working directory [$PWD] content:" && echo "$(ls $PWD)" && \
    echo "### Artifacts directory content:" && echo "$(ls /artifacts/)"
