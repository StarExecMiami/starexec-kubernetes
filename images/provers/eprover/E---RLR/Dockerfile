#------------------------------------------------------------
FROM eprover AS builder
FROM tptp-world-build

ENV PATH=".:${PATH}"
WORKDIR /artifacts

# E-specific stuff from ostensibly external image
COPY --from=builder /artifacts/* /artifacts/

#ENTRYPOINT ["runsolver", "--timestamp"]
ENTRYPOINT ["runsolver"]
#------------------------------------------------------------
