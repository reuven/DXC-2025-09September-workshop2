#!/usr/bin/env python3

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser()

# add arguments
parser.add_argument('files', nargs='*', type=argparse.FileType('r'))

# parse the arguments, putting them into a new namespace
args = parser.parse_args()
