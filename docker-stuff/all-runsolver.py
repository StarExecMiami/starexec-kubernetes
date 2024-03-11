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
        'i': args.intent,
        'b': "/artifacts/CWD/benchmark",
        'c': args.wall_clock_limit,
    }
    return ' '.join([parts[c] for c in args.runscript_format])


if __name__ == "__main__":
    parser = argparse.ArgumentParser("A script that wraps a podman call to a prover image")
    parser.add_argument("problem")
    parser.add_argument("-c", "--cpu-limit", default=300, type=int, help="Max CPU time in seconds")
    parser.add_argument("-w", "--wall-clock-limit", default=300, type=int, help="Max wall clock time in seconds")
    parser.add_argument("-m", "--memory-limit", default=-1, type=int, help="Max memory usage in MB")
    parser.add_argument("--intent", default="THM", choices=["THM", "SAT"], help="specify intent (THM, SAT, etc)")
    parser.add_argument("--dry-run", action="store_true", help="dry run")
    parser.add_argument("--image-name", default="eprover:3.0.03-runsolver", help="specify image name")
    parser.add_argument("-r", "--runscript", default="run_E", help="The script runsolver runs")
    parser.add_argument("-f","--runscript_format", default="")
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
    

