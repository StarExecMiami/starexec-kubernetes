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

# copy built stuff to artifacts
RUN cp ServiceTools/JJUsers/SPCForProblem /artifacts/
RUN cp TPTP4X/tptp4X /artifacts/
