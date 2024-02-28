#!/usr/bin/env python3

import argparse
import subprocess
import os
import shutil

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("problem")
    parser.add_argument("--cpu-limit", default=300, type=int, help="max CPU time in seconds")
    parser.add_argument("--wall-clock-limit", default=300, type=int, help="max wall clock time in seconds")
    parser.add_argument("--memory-limit", default=-1, type=int, help="max memory usage in MB")
    parser.add_argument("--intent", default="THM", choices=["THM", "SAT"], help="specify intent")
    parser.add_argument("--dry-run", action="store_true", help="dry run")
    parser.add_argument("--image-name", default="eprover:3.0.03-runsolver", help="specify image name")

    args = parser.parse_args()

    # get base name:
    problemBase = os.path.basename(args.problem)

    runsolver_args = f"-C {args.cpu_limit} -W {args.wall_clock_limit}"
    if args.memory_limit > 0:
        runsolver_args += f" -M {args.memory_limit}"

    run_E_args = f"/artifacts/CWD/benchmark {args.wall_clock_limit} {args.intent}"

    command = f"podman run -v .:/artifacts/CWD -t {args.image_name} --timestamp {runsolver_args} run_E {run_E_args}"
    if args.dry_run:
        print(command)
    else:
        shutil.copy(args.problem, "./benchmark")
        subprocess.run(command, shell=True)
        os.remove("./benchmark")
    

