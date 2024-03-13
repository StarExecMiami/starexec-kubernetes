#!/usr/bin/env python3

import argparse
import subprocess
import os
import shutil


def getRunsolverArgs(args):
    mem_part = f" -M {args.memory_limit}" if args.memory_limit > 0 else ""
    return f"-C {args.cpu_limit} -W {args.wall_clock_limit}{mem_part}"


def getRunscriptArgs(args):
    parts = {
        'P': "/artifacts/CWD/benchmark",
        'C': args.cpu_limit,
        'W': args.wall_clock_limit,
        'I': args.intent,
        'M': args.memory_limit,
    }
    return ' '.join([str(parts[c.upper()]) for c in args.runscript_args])


if __name__ == "__main__":
    parser = argparse.ArgumentParser("A script that wraps a podman call to a prover image")
    parser.add_argument("image_name", help="Image name e.g., eprover:3.0.03-runsolver-arm64")
    parser.add_argument("runscript", help="The system script and its args, e.g., 'run_E PWI'")
    # parser.add_argument("-f","--runscript_args", default="P", help="A string for the args (PCWI)")
    parser.add_argument("problem")
    parser.add_argument("-C", "--cpu-limit", default=60, type=int, help="Max CPU time in seconds")
    parser.add_argument("-W", "--wall-clock-limit", default=60, type=int, help="Max wall clock time in seconds")
    parser.add_argument("-M", "--memory-limit", default=-1, type=int, help="Max memory usage in MB")
    parser.add_argument("-I", "--intent", default="THM", choices=["THM", "SAT"], help="specify intent (THM, SAT, etc)")
    parser.add_argument("--dry-run", action="store_true", help="dry run")
    args = parser.parse_args()

    # Define podman command
    command = f"podman run -v .:/artifacts/CWD -t {args.image_name} --timestamp {getRunsolverArgs(args)} {args.runscript} {getRunscriptArgs(args)}"

    # Run command or print for dry run
    if args.dry_run:
        print(command)
    else:
        shutil.copy(args.problem, "./benchmark")
        subprocess.run(command, shell=True)
        os.remove("./benchmark")
    
