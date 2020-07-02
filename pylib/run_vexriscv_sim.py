#!/usr/bin/env python3

# Python module to run programs on a stm32f4-discovery board

# Copyright (C) 2019 Embecosm Limited
#
# Contributor: Jeremy Bennett <jeremy.bennett@embecosm.com>
#
# This file is part of Embench.

# SPDX-License-Identifier: GPL-3.0-or-later

"""
Embench module to run benchmark programs.

This version is suitable for a gdbserver with simulator.
"""

__all__ = [
    'get_target_args',
    'build_benchmark_cmd',
    'decode_results',
]

import argparse
import re

from embench_core import log

cpu_mhz = 1

def get_target_args(remnant):
    """Parse left over arguments"""
    parser = argparse.ArgumentParser(description='Get target specific args')

    parser.add_argument(
        '--regression-path',
        type=str,
        help='',
    )
    parser.add_argument(
        '--regression-args',
        type=str,
        help='',
    )
    parser.add_argument(
        '--cpu-mhz',
        type=int,
        default=1,
        help='Processor clock speed in MHz'
    )

    return parser.parse_args(remnant)


def build_benchmark_cmd(bench, args):
    """Construct the command to run the benchmark.  "args" is a
       namespace with target specific arguments"""
    global cpu_mhz
    cpu_mhz = args.cpu_mhz

    gen_hex = f'riscv64-unknown-elf-objcopy -O ihex {bench} {bench}.hex; HEX=$PWD'
    run_test = f'cd {args.regression_path}; make clean run {args.regression_args} RUN_HEX=$HEX/{bench}.hex'
    cmd = ['sh', '-c',f'{gen_hex};{run_test}']
    return cmd


def decode_results(stdout_str, stderr_str):
    """Extract the results from the output string of the run. Return the
       elapsed time in milliseconds or zero if the run failed."""
    #print("OUT")
    #print(stdout_str)
    #print("ERR")
    #print(stderr_str)

    

    # The start and end cycle counts are in the stderr string
    start_at = re.search('mTime 1 : (\d+)', stdout_str, re.S)
    end_at = re.search('mTime 2 : (\d+)', stdout_str, re.S)

    if not start_at or not end_at:
        log.debug('Warning: Failed to find timing')
        return 0.0
    
    time = int(end_at.group(1)) - int(start_at.group(1))

    # print(time)
    # Time from cycles to milliseconds
    global cpu_mhz
    return time / cpu_mhz / 1000.0
