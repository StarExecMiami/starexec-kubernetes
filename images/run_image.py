#!/usr/bin/env python3

import argparse
import subprocess
import os, sys
import shutil


def getRunsolverArgs(args):
    mem_part = f" -M {args.memory_limit}" if args.memory_limit > 0 else ""
    return "--timestamp --watcher-data /dev/null -C " + \
f"{args.cpu_limit} -W {args.wall_clock_limit}{mem_part}"



def getEnvVars(args):
    return " ".join([f"-e {k}='{v}'" for k, v in [
        ("RLR_INPUT_FILE", "/artifacts/CWD/problemfile"),
        ("RLR_CPU_LIMIT", args.cpu_limit),
        ("RLR_WC_LIMIT", args.wall_clock_limit),
        ("RLR_MEM_LIMIT", args.memory_limit),
        ("RLR_INTENT", args.intent),
    ]])


def makeBenchmark(problem):
    if problem:
        shutil.copy(problem, "./problemfile")
    else:
        with open('./problemfile', 'w') as problemfile:
            problemfile.write(sys.stdin.read())


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Wrapper for a podman call to a prover image")
    parser.add_argument("image_name", 
help="Image name, e.g., eprover:3.0.03-runsolver-arm64")
    parser.add_argument("-P", "--problem", 
help="Problem file if not stdin")
    parser.add_argument("-C", "--cpu-limit", default=-1, type=int, 
help="CPU time limit in seconds, default=60")
    parser.add_argument("-W", "--wall-clock-limit", default=-1, type=int, 
help="Wall clock time limit in seconds, default=60")
    parser.add_argument("-M", "--memory-limit", default=-1, type=int, 
help="Memory limit in MB, default=none")
    parser.add_argument("-I", "--intent", default="THM", choices=["THM", "SAT"], 
help="Intention (THM, SAT, etc), default=THM")
    parser.add_argument("--dry-run", action="store_true", 
help="dry run")
    args = parser.parse_args()

    # Format arguments
    runsolverArgs = getRunsolverArgs(args)


    command = f"podman run {getEnvVars(args)} -v .:/artifacts/CWD -t " + \
f"{args.image_name} {runsolverArgs} run_system"


    # Run command or print for dry run
    if args.dry_run:
        print(command)
    else:
        makeBenchmark(args.problem)
        subprocess.run(command, shell=True)
        os.remove("./problemfile")
    

