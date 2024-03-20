#!/usr/bin/env python3

import argparse
import subprocess
import os
import shutil


def getRunsolverArgs(args):
    mem_part = f" -M {args.memory_limit}" if args.memory_limit > 0 else ""
    return f"-C {args.cpu_limit} -W {args.wall_clock_limit}{mem_part}"


def getRunscriptArgs(args, args_format):
    parts = {
        'P': "/artifacts/CWD/benchmark",
        'C': args.cpu_limit,
        'W': args.wall_clock_limit,
        'I': args.intent,
        'M': args.memory_limit,
    }
    return ' '.join([str(parts[c.upper()]) for c in args_format])


if __name__ == "__main__":
    parser = argparse.ArgumentParser("A script that wraps a podman call to a prover image")
    parser.add_argument("image_name", help="Image name e.g., eprover:3.0.03-runsolver-arm64")
    parser.add_argument("--runscript", default="run PCWMI", help="The system script and its args, e.g., 'run_E PWI'")
    parser.add_argument("-P", "--problem", help="Problem file if not stdin")
    parser.add_argument("-C", "--cpu-limit", default=60, type=int, help="Max CPU time in seconds")
    parser.add_argument("-W", "--wall-clock-limit", default=60, type=int, help="Max wall clock time in seconds")
    parser.add_argument("-M", "--memory-limit", default=-1, type=int, help="Max memory usage in MB")
    parser.add_argument("-I", "--intent", default="THM", choices=["THM", "SAT"], help="specify intent (THM, SAT, etc)")
    parser.add_argument("--dry-run", action="store_true", help="dry run")
    args = parser.parse_args()

    # Format arguments
    runsolverArgs = getRunsolverArgs(args)
    runscript, runscriptArgsFormat = args.runscript.split()
    runscriptArgs = getRunscriptArgs(args, runscriptArgsFormat)

    # Construct podman command
    command = f"podman run -v .:/artifacts/CWD -t {args.image_name} --timestamp {runsolverArgs} {runscript} {runscriptArgs}"

    # Run command or print for dry run
    if args.dry_run:
        print(command)
    else:
        shutil.copy(args.problem, "./benchmark")
        subprocess.run(command, shell=True)
        os.remove("./benchmark")
    

