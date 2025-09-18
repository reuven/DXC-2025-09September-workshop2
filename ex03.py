#!/usr/bin/env python3

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser()

# add arguments for name and company
parser.add_argument('first')
parser.add_argument('op')
parser.add_argument('second')

# parse the arguments, putting them into a new namespace
args = parser.parse_args()
