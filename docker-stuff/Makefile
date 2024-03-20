.PHONY: base provers eprover iprover leo3 vampire

# Current versions of each prover as variables:
EPROVER_VERSION = 3.0.03
VAMPIRE_VERSION = 4.8
LEO3_VERSION = 1.7.0

# High level targets ########################################################
all: base provers

base: ubuntu-build scala-build tptp-world-build

provers: eprover leo3 vampire

# Prerequisite targets ######################################################
ubuntu-build:
	podman build -t ubuntu-build ./base-build/ubuntu-build

scala-build:
	podman build -t scala-build ./base-build/scala-build

tptp-world-build: ubuntu-build
	podman build -t tptp-world-build ./base-build/tptp-world-build



#############################################################################
# Targets for each prover ###################################################
#############################################################################

# Eprover targets: #########################################################
eprover: ubuntu-build eprover-build eprover-runsolver

eprover-build: tptp-world-build
	podman build -t eprover-build ./provers/eprover/E---$(EPROVER_VERSION)/build

eprover-runsolver: eprover-build
	podman build -t eprover:$(EPROVER_VERSION)-runsolver ./provers/eprover/E---runsolver


# Vampire targets: ###########################################################
vampire: ubuntu-build vampire-build vampire-runsolver

vampire-build: 
	podman build -t vampire-build ./provers/vampire/Vampire---$(VAMPIRE_VERSION)/build

vampire-runsolver: 
	podman build -t vampire:$(VAMPIRE_VERSION)-runsolver ./provers/vampire/Vampire---runsolver


# Leo3 targets: #############################################################
leo3: scala-build leo3-build leo3-runsolver

leo3-build: 
	podman build -t leo3-build ./provers/leo3/Leo-III---$(LEO3_VERSION)/build

leo3-runsolver: 
	podman build -t leo3:$(LEO3_VERSION)-runsolver ./provers/leo3/Leo---runsolver

