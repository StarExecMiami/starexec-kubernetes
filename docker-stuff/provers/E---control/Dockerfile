FROM e---3.0.03-build AS builder
FROM alpine:latest
RUN apk update && apk add --no-cache tcsh

ENV PATH=".:${PATH}"
WORKDIR /artifacts

COPY --from=builder /artifacts/eprover /artifacts/
COPY --from=builder /artifacts/eprover-ho /artifacts/
ADD run_E /artifacts/run_E
ADD tptp4X /artifacts/tptp4X
ADD SPCForProblem /artifacts/SPCForProblem

ENTRYPOINT ["run_E"] 
