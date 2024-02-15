FROM ubuntu-build

ARG VAMPIRE_VERSION=v4.7
RUN git clone --depth 1 --branch $VAMPIRE_VERSION https://github.com/vprover/vampire.git

# Set working directory to cloned sources directory
WORKDIR vampire

RUN mkdir /tmp/build && cd /tmp/build

RUN cmake /vampire

RUN make

RUN cp bin/vampire* /artifacts/

# Smoke tests
RUN echo "############ Smoke tests ############" && \
    /artifacts/vampire* /vampire/regressions/problems/tptp_out_intro_ssat.p | grep "SZS status Unsatisfiable"

RUN echo "### Working directory [$PWD] content:" && echo "$(ls $PWD)" && \
    echo "### Artifacts directory content:" && echo "$(ls /artifacts/)"

