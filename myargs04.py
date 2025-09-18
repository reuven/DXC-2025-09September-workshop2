#!/usr/bin/env python3

# loading the module
import argparse

# creating the parser
parser = argparse.ArgumentParser()

# add arguments for name and company
parser.add_argument('first', type=int)
parser.add_argument('op')
parser.add_argument('second', type=int, default=10)

parser.add_argument('age', type=float)

# parse the arguments, putting them into a new namespace
args = parser.parse_args()

# grab the names via attributes on "args"
print(f'Next year, {args.name} will be {args.age + 1} years old!')
