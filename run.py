#!/usr/bin/env python3

import sys
import subprocess

import numpy as np

from utils import *


class bcolors:
    """thanks https://stackoverflow.com/questions/287871/print-in-terminal-with-colors"""

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def run(model, dataset):
    with open(dataset) as stdin:
        process = subprocess.run(
            ['python', model],
            stdin=stdin,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf8',
        )
        # err(process)
        if process.returncode != 0:
            err(f"returncode={process.returncode}")
        err(f"{bcolors.OKBLUE}stdout:{bcolors.ENDC} {process.stdout}")
        err(f"{bcolors.WARNING}stderr:{bcolors.ENDC} {process.stderr}")


def main():
    files = sys.argv[1:]
    # err(files)
    models = [file for file in files if file.endswith('.py')]
    datasets = [file for file in files if file.endswith('.txt') or file.endswith('.in')]

    if not models:
        err("no model in args (.py file)")
        exit(1)
    if not datasets:
        err("no dataset in args (.txt or .in file)")
        exit(1)

    for file in files:
        if file not in models and file not in datasets:
            err(f"{bcolors.FAIL}unrecognized file arg: {file}{bcolors.ENDC}")
            # exit(1)

    for dataset in datasets:
        for model in models:
            err(bcolors.HEADER + f"{model} {dataset}" + bcolors.ENDC)
            run(model, dataset)


if __name__ == '__main__':
    main()
