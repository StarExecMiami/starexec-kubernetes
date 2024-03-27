FROM eprover-build AS builder

FROM alpine:latest

# This is "broken"
COPY --from=builder /artifacts/eprover /usr/bin/
COPY --from=builder /artifacts/eprover-ho /usr/bin/

# ENTRYPOINT ["eprover-ho"]
ENTRYPOINT ["eprover"] # alternative entrypoint if using only first-order reasoning
