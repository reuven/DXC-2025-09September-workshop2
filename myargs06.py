#!/usr/bin/env python3

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument('file', type=file)

# parse the arguments, putting them into a new namespace
args = parser.parse_args()

for one_line in args.file:
    print(len(one_line), end=' ')
