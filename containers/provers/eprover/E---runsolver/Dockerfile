#------------------------------------------------------------
FROM eprover-build AS builder
FROM tptp-world-build

ENV PATH=".:${PATH}"
WORKDIR /artifacts

# E-specific stuff from ostensibly external image
COPY --from=builder /artifacts/eprover /artifacts/
COPY --from=builder /artifacts/eprover-ho /artifacts/

# run_container script 
ADD run_container /artifacts/

# run_E script 
ADD run_E /artifacts/

#ENTRYPOINT ["runsolver", "--timestamp"]
ENTRYPOINT ["runsolver"]
#------------------------------------------------------------
