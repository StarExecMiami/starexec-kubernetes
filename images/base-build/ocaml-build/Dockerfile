FROM ocaml/opam:debian

# Install dependencies (seems to require sudo.. why?)
RUN sudo apt-get update && \
    sudo apt-get install -y --no-install-recommends libgmp-dev zlib1g-dev

# Install OCAML
RUN opam switch create 4.14.1+flambda --package=ocaml-variants.4.14.1+options,ocaml-option-flambda

# Update the current shell environment
RUN eval $(opam env)

# Install more dependencies
RUN opam install ocamlfind ocamlgraph zarith yojson

# Update the current shell environment
RUN eval $(opam env)

ENTRYPOINT ["/bin/bash"]
