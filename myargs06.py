#!/usr/bin/env python3

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument('filename')

# parse the arguments, putting them into a new namespace
args = parser.parse_args()

with open(args.filename) as f:
    for one_line in f:
        print(len(one_line), end=' ')
