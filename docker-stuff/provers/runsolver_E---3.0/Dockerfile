FROM eprover-build AS builder

FROM alpine:latest

COPY --from=builder /artifacts/eprover /usr/bin/
COPY --from=builder /artifacts/eprover-ho /usr/bin/

# Install dependencies
RUN apk add --upgrade git g++ make numactl numactl-dev

# Download runsolver:
RUN git clone https://github.com/utpalbora/runsolver.git

# Build runsolver from /runsolver/src using make.
WORKDIR /runsolver/src
RUN make

# Run runsolver
ENTRYPOINT ["/runsolver/src/runsolver"]





# ENTRYPOINT ["eprover-ho"]
# ENTRYPOINT ["eprover"] # alternative entrypoint if using only first-order reasoning

