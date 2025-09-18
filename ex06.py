#!/usr/bin/env python3
# reverse.py

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser(description='Reverse lines of a file')

# add arguments for name and company
parser.add_argument('-i', '--infilename', type=argparse.FileType('r'),
                    help='Input file', required=True)
parser.add_argument('-o', '--outfilename', type=argparse.FileType('w'),
                    help='Output file', required=False)

# parse the arguments, putting them into a new namespace
args = parser.parse_args()
