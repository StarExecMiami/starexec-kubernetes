FROM alpine:latest
RUN apk update && apk add --no-cache tcsh git
RUN git clone --recurse-submodules https://github.com/TPTPWorld/ServiceTools.git
RUN git clone --recurse-submodules https://github.com/TPTPWorld/TPTP4X.git
ENV TPTP_HOME .
RUN cd ServiceTools/JJUsers && make SPCForProblem 
RUN cd TPTP4X && make tptp4X
RUN cp ServiceTools/JJUsers/SPCForProblem /artifacts/
RUN cp TPTP4X/tptp4X /artifacts/
