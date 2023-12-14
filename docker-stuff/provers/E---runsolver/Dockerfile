FROM e---3.0.03-build AS builder
FROM tptp-world-build

RUN apk update && apk add --no-cache tcsh 

ENV PATH=".:${PATH}"
WORKDIR /artifacts

# E-specific stuff from ostensibly external image
COPY --from=builder /artifacts/eprover /artifacts/
COPY --from=builder /artifacts/eprover-ho /artifacts/

# run_E script 
ADD run_E /artifacts/

ENTRYPOINT ["runsolver"]