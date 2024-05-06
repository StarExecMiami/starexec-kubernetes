#------------------------------------------------------------
ARG PROVER_IMAGE

FROM ${PROVER_IMAGE} AS builder
FROM tptp-world-build

ENV PATH=".:${PATH}"
WORKDIR /artifacts

# System specific stuff 
COPY --from=builder /artifacts/* /artifacts/

#ENTRYPOINT ["ResourceLimitedRun"]
ENTRYPOINT ["runsolver"]
#------------------------------------------------------------
