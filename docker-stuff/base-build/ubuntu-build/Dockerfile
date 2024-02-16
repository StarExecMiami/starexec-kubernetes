FROM ubuntu:latest

# Install gcc, make & co, also GIT
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential cmake git tcsh

# Configure GIT to clone repos
RUN export GIT_SSL_NO_VERIFY=1 && \
    git config --global http.sslverify false

# Configure GIT to clone repos
RUN export GIT_SSL_NO_VERIFY=1 && \
    git config --global http.sslverify false

# Create "/artifacts" directory for build artifacts
RUN mkdir /artifacts/

ENTRYPOINT ["/bin/bash"]
